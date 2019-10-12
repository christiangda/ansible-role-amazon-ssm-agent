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
        assert True
        # Snap is a service, so over docker images we don't have it
        # f = host.file('/snap/amazon-ssm-agent/current/amazon-ssm-agent')
        # assert f.exists
        # assert f.user == 'root'
        # assert f.group == 'root'
    else:
        pkg = host.package('amazon-ssm-agent')
        assert pkg.is_installed
