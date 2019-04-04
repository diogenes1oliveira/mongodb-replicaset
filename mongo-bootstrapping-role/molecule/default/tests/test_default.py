from contextlib import contextmanager
import os
import uuid
import time

import pytest
import testinfra.utils.ansible_runner
from yaml import load as yaml_load

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture(scope='module')
def reboot(host):
    host.ansible('reboot', {'reboot_timeout': 60}, check=False)


@pytest.fixture(scope='module')
def ansible(host):
    def call_ansible_module(module_name, check=False, become=True, **kwargs):
        return host.ansible(module_name, kwargs, check=check, become=True)

    return call_ansible_module


def test_package_versions(host):
    assert '4.0' in host.check_output('mongo --version')
    assert host.package('jq').is_installed

    pip_packages = set(host.pip_package.get_packages().keys())
    assert 'pymongo' in pip_packages


def test_thp_is_disabled(reboot, host):
    paths = [
        '/sys/kernel/mm/transparent_hugepage/enabled',
        '/sys/kernel/mm/redhat_transparent_hugepage/enabled',
    ]
    for path in paths:
        file = host.file(path)
        assert not file.exists or file.contains('[never]')


def test_can_use_mongo(reboot, host):
    hash = str(uuid.uuid4())

    mongo_drop = "db.smoke_collection.drop()"
    mongo_insert = f"db.smoke_collection.insertOne({{value: '{hash}'}})"
    mongo_query = "print(db.smoke_collection.findOne().value)"

    mongo_auth = '-u root -p 12345678 --authenticationDatabase admin'
    host.run_test(f'mongo {mongo_auth} smoke_database --eval "{mongo_drop}"')
    host.run_test(f'mongo {mongo_auth} smoke_database --eval "{mongo_insert}"')
    cmd_query = f'mongo {mongo_auth} smoke_database --eval "{mongo_query}"'

    assert hash in host.check_output(cmd_query)


@contextmanager
def config_saver_test(host):
    # save a new UUID in the configuration file
    hash = str(uuid.uuid4())
    host.run_expect([0], f'sudo su -c "echo \'# {hash}\' >> /etc/mongod.conf"')

    yield
    time.sleep(0.2)

    conf = host.file('/etc/mongod.current.conf').content_string
    assert hash in conf


def test_is_saving_config(host, ansible):
    ansible('systemd', name='mongod', state='restarted')

    with config_saver_test(host):
        ansible('systemd', name='mongod', state='stopped')
        ansible('systemd', name='mongod', state='started')

    ansible('systemd', name='mongod', state='restarted')
    ansible('systemd', name='mongod', state='stopped')

    with config_saver_test(host):
        ansible('systemd', name='mongod', state='started')

    with config_saver_test(host):
        ansible('systemd', name='mongod', state='restarted')


def test_is_shutting_down_cleanly(host, ansible):
    ansible('systemd', name='mongod', state='restarted')

    conf = host.file('/etc/mongod.current.conf').content_string
    pid_path = yaml_load(conf)['processManagement']['pidFilePath']

    ansible('systemd', name='mongod', state='stopped')
    assert not host.file(pid_path).exists

    ansible('systemd', name='mongod', state='started')
    assert host.file(pid_path).exists
    ansible('systemd', name='mongod', state='stopped')
    assert not host.file(pid_path).exists


def test_can_start_cleanly(host, ansible):
    ansible('systemd', name='mongod', state='stopped')
    conf = host.file('/etc/mongod.conf').content_string
    port = yaml_load(conf)['net']['port']

    host.run_expect([0], 'sudo mongod-clean-startup')
    host.run_expect([0], f" mongo --port {port} --eval 'quit()' ")

    # idempotence
    host.run_expect([0], 'sudo mongod-clean-startup')
    host.run_expect([0], f" mongo --port {port} --eval 'quit()' ")

    # started via systemctl
    ansible('systemd', name='mongod', state='restarted')
    host.run_expect([0], 'sudo mongod-clean-startup')
    host.run_expect([0], f" mongo --port {port} --eval 'quit()' ")
