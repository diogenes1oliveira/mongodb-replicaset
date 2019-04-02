mongo-baker
=========

Bakes an AMI image with mongo pre-installed.

Requirements
------------

Currently, it only works on base systems that use the YUM package manager.

Role Variables
--------------

None required.

How to use it
-------------

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