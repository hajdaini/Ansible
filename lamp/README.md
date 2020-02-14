LAMP
=========

This playbook allows you to install a web server (apache + php + custom packages)
with a test web app and a database server(mysql) with a custom user and table.

Requirements
------------

Debian os family or RedHat OS family

Roles
--------------

- web : [Documentation here](roles/web/README.md)
- database : [Documentation here](roles/database/README.md)

> On the above documentation, you will find the different mandatory variables of the roles

Dependencies
------------

n/a

Usage
----------------

- Create a vault :
  ```sh
  ansible-vault create vars/mysql-users.yml
  ```
- Put the mysql sensitive data in your current vault file :
  ```yaml
  ---
  mysql_user: "user"
  mysql_password: "your password"
  root_password: "your password"
  ```
- Run the playbook :
  ```sh
  ansible-playbook playbook.yml --ask-vault-pass
  ```  

License
-------

BSD

Author Information
------------------

[https://devopssec.fr/](https://devopssec.fr/)

