# Ansible Role: christiangda.amazon_ssm_agent

[![Build Status](https://travis-ci.org/christiangda/ansible-role-amazon-ssm-agent.svg?branch=master)](https://travis-ci.org/christiangda/ansible-role-amazon-ssm-agent)
[![Ansible Role](https://img.shields.io/ansible/role/39604.svg)](https://galaxy.ansible.com/christiangda/amazon_cloudwatch_agent)

This role [Install AWS Systems Manager Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)

**Features:**

* Downloads and installs AWS System Manager Agent from AWS distribution package
* Rotate the Agent Log file

## Requirements

This role works on RedHat, CentOS, Oracle, Amazon Linux, Debian and Ubuntu distributions

* RedHat/CentOS/Oracle
  * 6
  * 7
  * 8
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

To see the compatibility matrix of Python vs. Ansible see the project [Travis-CI build matrix](https://travis-ci.org/christiangda/ansible-role-amazon-ssm-agent)

## Role Variables

```yaml
# possible values:
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

### RedHat/CentOS/Oracle, Ubuntu and Debian

```yaml
- hosts: servers
    gather_facts: True
    roles:
        - role: christiangda.amazon_ssm_agent
            vars:
                ssm_update: true
```

### Amazon Linux 1/2 (my-playbook.yml)

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

**Inventory file sample (inventory)**

```ini
[all]
10.14.x.y
10.14.v.z

[amazon-1]
10.14.x.y

[amazon-2]
10.14.v.z
```

**How to used it**

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

**Prepare your environment**

**Python 3**

```bash
mkdir ansible-roles
cd ansible-roles/

python3 -m venv venv
source venv/bin/activate
pip install pip --upgrade
pip install ansible
pip install molecule">=2.22rc1"
pip install molecule[vagrant]
pip install selinux
pip install docker
pip install pytest
pip install pytest-mock
pip install pylint
pip install rope
pip install autopep8
pip install yamllint
pip install flake8
```

**Python 2.7**

Dependencies

```bash
sudo dnf install redhat-rpm-config
sudo dnf install python-devel
sudo dnf install libselinux-python
```

```bash
mkdir ansible-roles
cd ansible-roles/

python2.7 -m virtualenv venv
source venv/bin/activate
pip install pip --upgrade
pip install ansible
pip install molecule">=2.22rc1"
pip install molecule[vagrant]
pip install selinux
pip install docker
pip install pytest
pip install pytest-mock
pip install pylint
pip install rope
pip install autopep8
pip install yamllint
pip install flake8
```

**Clone the role repository and create symbolic link**

```bash
git clone https://github.com/christiangda/ansible-role-amazon-ssm-agent.git
ln -s ansible-role-amazon-ssm-agent christiangda.amazon_ssm_agent
cd christiangda.amazon_ssm_agent
```

**Execute the test**

Using docker in local

```bash
molecule test [--scenario-name default]
```

Using vagrant in local

```bash
molecule create --scenario-name vagrant
molecule converge --scenario-name vagrant
molecule verify --scenario-name vagrant
```

or

```bash
molecule test --scenario-name vagrant
```

**Additionally if you want to test using VMs, I have a very nice [ansible-playground project](https://github.com/christiangda/ansible-playground) that use Vagrant and VirtualBox, try it!.**

## License

This module is released under the GNU General Public License Version 3:

* [http://www.gnu.org/licenses/gpl-3.0-standalone.html](http://www.gnu.org/licenses/gpl-3.0-standalone.html)

## Author Information

* [Christian González Di Antonio](https://github.com/christiangda)
