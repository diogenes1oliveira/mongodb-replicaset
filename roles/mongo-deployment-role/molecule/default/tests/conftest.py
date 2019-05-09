import pytest

@pytest.fixture(scope='module')
def ansibler(host):
    def call_ansible_module(module_name, check=False, become=True, **kwargs):
        return host.ansible(module_name, kwargs, check=check, become=become)

    return call_ansible_module
