from datetime import datetime
import os
import subprocess

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_log_rotation(host):
    for i in range(10):
        assert host.run(
            'mongo --authenticationDatabase admin' +
            f'-u root -p 12345678 --eval "quit()"'
        ).rc == 0

    date_now = host.run('date +%Y-%m-%d').stdout.strip()
    assert not host.file(f'/var/mongodb-rs/log/mongod.log-{date_now}').exists

    cmd = host.run(
        'logrotate --verbose /etc/logrotate.d/mongod-log-rotate.conf'
    )
    assert cmd.rc == 0
    assert host.file(f'/var/mongodb-rs/log/mongod.log-{date_now}').exists
