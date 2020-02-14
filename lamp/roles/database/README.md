database
=========

Install mysql database with a custom user and table.

Requirements
------------

Debian os family or RedHat OS family

Role Variables
--------------

| name                    | type   | description                                                                       | mandatory |
|-------------------------|--------|-----------------------------------------------------------------------------------|-----------|
| `mysql_user`            | string | Mysql user that will be created                                                   |   yes     |
| `mysql_password`        | string | Mysql password that will be created                                               |   yes     |
| `mysql_dbname`          | string | Database name that will be created with all privileges grant for the `mysql_user` |   yes     |
| `webserver_host`        | string | Web server ip/host that can access the `mysql_dbname` database                    |   yes     |
| `root_password`         | list   | the new root password                                                             |   yes     |

Dependencies
------------

n/a

Example Playbook
----------------

```yaml
- hosts: db
  become: yes
  vars: vars/main.yml
    - mysql_user: "admin"
    - mysql_password: "Test_34535$"
    - mysql_dbname: "blog"
    - webserver_host: "192.168.0.21"
    - root_password: "Test_68670$" 

  roles:
    - database
```

License
-------

BSD

Author Information
------------------

[https://devopssec.fr/](https://devopssec.fr/)

