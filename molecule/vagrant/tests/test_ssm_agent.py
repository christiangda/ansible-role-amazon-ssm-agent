import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_amazon_ssm_agent_is_installed(host):
    os = host.system_info.distribution.lower()
    rl = host.system_info.release

    # Ubuntu is installed using snap package
    if ((os == 'ubuntu' and rl.split('.')[0] == '16') or
            (os == 'ubuntu' and rl.split('.')[0] == '18')):
        f = host.file('/snap/amazon-ssm-agent/current/amazon-ssm-agent')
        assert f.exists
        assert f.user == 'root'
        assert f.group == 'root'
    else:
        pkg = host.package('amazon-ssm-agent')
        assert pkg.is_installed


def test_amazon_ssm_agent_running_and_enabled(host):
    os = host.system_info.distribution.lower()
    rl = host.system_info.release

    if os == 'centos' and rl.split('.')[0] == '6':
        p = host.process.get(user="root", comm="amazon-ssm-agen")
        assert p is not None

    # Ubuntu is installed using snap package
    elif ((os == 'ubuntu' and rl.split('.')[0] == '16') or
          (os == 'ubuntu' and rl.split('.')[0] == '18')):
        amazon_ssm_agent = host.service(
            'snap.amazon-ssm-agent.amazon-ssm-agent')
        assert amazon_ssm_agent.is_running
        assert amazon_ssm_agent.is_enabled
    else:
        amazon_ssm_agent = host.service('amazon-ssm-agent')
        assert amazon_ssm_agent.is_running
        assert amazon_ssm_agent.is_enabled
