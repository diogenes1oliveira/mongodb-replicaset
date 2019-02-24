mongo-baker
=========

Bakes an AMI image with mongo pre-installed.

Requirements
------------

Currently, it only works on base systems that use the YUM package manager.

Role Variables
--------------

**dbpath**: base path for Mongo directories. Defaults to `/usr/db`.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, dbpath: '/usr/db' }

License
-------

MIT

Author Information
------------------

Diógenes Oliveira
diogenes1oliveira@gmail.com