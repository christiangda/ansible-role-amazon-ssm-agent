# Ansible Role: christiangda.amazon-ssm-agent

[![Build Status](https://travis-ci.org/christiangda/ansible-role-amazon-ssm-agent.svg?branch=master)](https://travis-ci.org/christiangda/ansible-role-amazon-ssm-agent)
[![Ansible Role](https://img.shields.io/ansible/role/39550.svg)](https://galaxy.ansible.com/christiangda/amazon_cloudwatch_agent)

This role [Install AWS Systems Manager Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)

**Functionality:**
* It downloads and installs AWS System Manager Agent from AWS OS distribution package
* It rotate the Agent Log

## Requirements

This role work on RedHat, CentOS, Amazon Linux, Debian and Ubuntu distributions

specific version:

* RedHat
  * 6
  * 7
* CentOS
  * 6
  * 7
* Amazon Linux
  * 1
  * 2
* Ubuntu
  * 16.*
  * 18.*
* Debian
  * jessie
  * sid
  * stretch

## Role Variables

**Files:**

* defaults/main.yml

```yaml
# posible values:
# - true
# - false
# default value: false
# notes:
# * set value to true when you want to update installed version
ssm_update: false
```

## Dependencies

None

## Example Playbook

### RedHat/CentOS, Ubuntu and Debian

```yaml
- hosts: servers
    gather_facts: True
    roles:
    - role: christiangda.amazon_ssm_agent
        vars:
            ssm_update: true
```

###  Amazon Linux 1/2 (my-playbook.yml)

```yaml
- hosts: all
    gather_facts: True
    become: true
    become_user: root
    become_method: sudo
    remote_user: ec2-user
    roles:
    - role: christiangda.amazon_ssm_agent
```

Inventory file sample (inventory)

```ini
[all]
10.14.x.y
10.14.v.z

[amazon-1]
10.14.x.y

[amazon-2]
10.14.v.z
```

How to used it

```bash
ansible-playbook my-playbook.yml \
    --inventory inventory \
    --private-key [~/location of my key.pem] \
    --become \
    --become-user=ec2-user \
    --user ec2-user
```

## Development / Contributing

This role is tested using [Molecule](https://molecule.readthedocs.io/en/latest/) and was developed using
[Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

Prepare your environment

```bash
mkdir ansible-roles
cd ansible-roles/

virtualenv --no-site-packages --python /usr/bin/python2.7 vend
source vend/bin/activate
pip install pip --upgrade
pip install pytest
pip install pytest-mock
pip install pylint
pip install rope
pip install autopep8
pip install yamllint
pip install molecule
pip install ansible
pip install docker-py
```

Clone the role repository and create symbolic link
```bash
git clone https://github.com/christiangda/ansible-role-amazon-ssm-agent.git
ln -s ansible-role-amazon-ssm-agent amazon-ssm-agent
cd ansible-role-amazon-ssm-agent
```

Execute the test
```bash
molecule test
```

Additionally if you want to test using VMs, I have a very nice [ansible-playground project](https://github.com/christiangda/ansible-playground) that use Vagrant and VirtualBox, try it!.

## License

This module is released under the GNU General Public License Version 3:

* [http://www.gnu.org/licenses/gpl-3.0-standalone.html](http://www.gnu.org/licenses/gpl-3.0-standalone.html)

## Author Information

* [Christian González Di Antonio](https://github.com/christiangda)
