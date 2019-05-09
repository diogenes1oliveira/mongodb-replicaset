import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_password_is_being_changed_from_default(ansibler):
    cmd = ansibler('mongo_shell', password='12345678', command='quit(0)')
    assert not cmd['authenticated']

    cmd = ansibler('mongo_shell', password='root-password', command='quit(0)')
    assert cmd['authenticated']