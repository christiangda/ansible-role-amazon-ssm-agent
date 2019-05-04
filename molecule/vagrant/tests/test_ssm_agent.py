import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_amazon_ssm_agent_is_installed(host):
    pkg = host.package('amazon-ssm-agent')

    assert pkg.is_installed


def test_amazon_ssm_agent_running_and_enabled(host):
    amazon_ssm_agent = host.service('amazon-ssm-agent')

    assert amazon_ssm_agent.is_running
    assert amazon_ssm_agent.is_enabled
