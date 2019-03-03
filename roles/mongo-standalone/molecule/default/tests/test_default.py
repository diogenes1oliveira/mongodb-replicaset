import json
import os
import uuid

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_can_login(host):
    hash = str(uuid.uuid4())

    mongo_login = (
        f"mongo --quiet --authenticationDatabase admin "
        f"--username root --password '12345678'"
    )
    mongo_drop = "db.smoke_collection.drop()"
    mongo_insert = f"db.smoke_collection.insertOne({{value: '{hash}'}})"
    mongo_query = "print(db.smoke_collection.findOne().value)"

    host.run_test(f'{mongo_login} smoke_database --eval "{mongo_drop}"')
    host.run_test(f'{mongo_login} smoke_database --eval "{mongo_insert}"')
    cmd_query = f'{mongo_login} smoke_database --eval "{mongo_query}"'

    assert hash in host.check_output(cmd_query)


def test_refuses_login(host):
    mongo_login = (
        f"mongo --authenticationDatabase admin "
        f"--username root --password '12345678-wrong-password'"
    )
    cmd = host.run(mongo_login)
    assert cmd.rc != 0
    assert 'Authentication failed' in cmd.stdout

    mongo_check_rs = (
        f"mongo --quiet --eval 'rs.status()'"
    )
    cmd = host.run(mongo_check_rs)
    assert json.loads(cmd.stdout)['codeName'] == 'Unauthorized'
