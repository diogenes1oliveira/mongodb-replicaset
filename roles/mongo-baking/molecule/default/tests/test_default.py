import os
import uuid

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture(scope='module')
def reboot(host):
    host.ansible('reboot', {'reboot_timeout': 60}, check=False)


def test_package_versions(host):
    assert '3.6' in host.check_output('mongo --version')
    assert host.package('jq').is_installed

    pip_packages = set(host.pip_package.get_packages().keys())
    assert 'pymongo' in pip_packages


def test_dhp_is_disabled(reboot, host):
    paths = [
        '/sys/kernel/mm/transparent_hugepage/enabled',
        '/sys/kernel/mm/redhat_transparent_hugepage/enabled',
    ]
    for path in paths:
        file = host.file(path)
        assert not file.exists or file.contains('[never]')


def test_dbpath_exists(host):
    assert host.file('/usr/db').exists


def test_can_use_mongo(reboot, host):
    hash = str(uuid.uuid4())

    mongo_drop = "db.smoke_collection.drop()"
    mongo_insert = f"db.smoke_collection.insertOne({{value: '{hash}'}})"
    mongo_query = "print(db.smoke_collection.findOne().value)"

    host.run_test(f'mongo --quiet smoke_database --eval "{mongo_drop}"')
    host.run_test(f'mongo --quiet smoke_database --eval "{mongo_insert}"')
    cmd_query = f'mongo --quiet smoke_database --eval "{mongo_query}"'

    assert hash in host.check_output(cmd_query)
