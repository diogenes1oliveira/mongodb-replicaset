mongo-baker
=========

Bakes an AMI image with mongo pre-installed.

Requirements
------------

Currently, it only works on base systems that use the YUM package manager.

Role Variables
--------------

**dbpath**: base path for Mongo directories. Defaults to `/usr/db`.

Example Playbook
----------------

Install and prepare Mongo in the instances:

    - hosts: servers
      roles:
         - { role: 'mongo-baker', dbpath: '/usr/db' }

License
-------

MIT

Author Information
------------------

Diógenes Oliveira
diogenes1oliveira@gmail.com