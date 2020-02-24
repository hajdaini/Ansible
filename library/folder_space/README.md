folder_space
============

Checks if a folder has enough storage space.

Module Variables
--------------

| name       | type   | description                               | mandatory |
|------------|--------|-------------------------------------------|-----------|
| `path`     | string | path of the file that will be analyzed    |   yes     |
| `size`     | string | comparison size                           |   yes     |


Example
-------

```yaml
- hosts: localhost
  tasks:
    - name: 'check folder size of /home/hatim'
      folder_space:
        path: '/home/hatim'
        size: '20g'
```

License
-------

BSD

Author Information
------------------

[https://devopssec.fr/](https://devopssec.fr/)
