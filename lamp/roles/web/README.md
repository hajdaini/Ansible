web
=========

install apache and php with a test web app.

Requirements
------------

Debian os family or RedHat OS family

Role Variables
--------------

| name                    | type   | description                                                     | mandatory |
|-------------------------|--------|-----------------------------------------------------------------|-----------|
| `mysql_user`            | string | Mysql user that will be used in the php app                     |   yes     |
| `mysql_password`        | string | Mysql password that will be used in the php app                 |   yes     |
| `mysql_dbname`          | string | Database name that will be used in the php app                  |   yes     |
| `db_host`               | string | Database ip/host that that will be used in the php app          |   yes     |
| `extra_packages_debian` | list   | extra Debian packages that will be downloaded                   |   no      |
| `extra_packages_redhat` | list   | extra RedHat packages that will be downloaded                   |   no      |

Dependencies
------------

n/a

Example Playbook
----------------

```yaml
- hosts: web
  become: yes
  vars: vars/main.yml
    - mysql_user: "admin"
    - mysql_password: "Test_34535$"
    - mysql_dbname: "blog"
    - db_host: "192.168.0.22"
    - extra_packages_debian: ['php-curl', 'php-gd', 'php-mbstring'] 
    - extra_packages_redhat: ['php-xml', 'php-gd', 'php-mbstring'] 

  roles:
    - web
```

License
-------

BSD

Author Information
------------------

[https://devopssec.fr/](https://devopssec.fr/)
