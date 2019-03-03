mongo-standalone
================

Sets up a MongoDB standalone instance.

Requirements
------------

**MongoDB** should already be installed in the target instances, preferrably
with the ```mongo-baking``` role in this repository.

Role Variables
--------------

```yaml
# defaults/main.yml
  admin_username: root
  admin_password: null # needs to be passed explicitly

# vars/main.yml
  # base path for MongoDB files
  dbpath: '/var/mongodb-replicaset'

  # port to bind to when in noauth mode
  port_noauth: 27020
```

Dependencies
------------

```
mongo-baking
```

How to use it
-------------

Deploy it passing the admin username and passwords for the instances. In case
you want to deploy a replica set, inform its name as well:

```yaml
# For a standalone
  - hosts: db-instance
    roles:
      - role: mongo-setup
        admin_username: root
        admin_password: '12345678'
```

License
-------

MIT

Author Information
------------------

Diógenes Oliveira
diogenes1oliveira@gmail.com
