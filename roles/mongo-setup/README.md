mongo-setup
===========

Sets up a MongoDB replica set or standalone instance.

Requirements
------------

**MongoDB** should already be installed in the target instances, preferrably
with the ```mongo-baking``` role in this repository.

To deploy a replica set, the instances need to be divided in the primary,
secondary and arbiter groups.

Role Variables
--------------

```yaml
# defaults/main.yml
  admin_username: root
  admin_password: null # needs to be passed explicitly
  replica_set: rs0     # a falsey value or the name for the replica set

# vars/main.yml
  # names of the groups for each role in the replica set
  primary_group: 'primary'
  secondary_group: 'secondary'
  arbiter_group: 'arbiter'

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
# For a replica set
  - hosts: db-instances
    roles:
      - role: mongo-setup
        admin_username: root
        admin_password: '12345678'
        replica_set: rs0

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
