mongo-boostrapping-role
=======================

Bootstraps a MongoDB installation.

Requirements
------------

Currently, it only works on base systems that use the YUM package manager.

Role Variables
--------------
```yaml
# defaults/main.yml
  
  # path to store the data files
  db_path: "/var/mongodb-rs/data"

  # path to store the runtime-specific files, such as PID files
  run_path: "/var/mongodb-rs/run"

  # path to store the logs
  log_path: "/var/mongodb-rs/log"

  # path to store misc files, such as keyfiles and certificates
  config_path: "/var/mongodb-rs/config"

  # port to bind to when in the no-auth mode
  # assure that no external traffic is allowed into this port.
  tcp_port_no_auth: 27020

  # force the generation and synchronization of the authentication files
  force_auth_update: false

  admin_username: root
  admin_password: null # needs to be passed explicitly
  replica_set: rs0     # name for the replica set

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

db_path: "/var/mongodb-rs/data"
run_path: "/var/mongodb-rs/run"
log_path: "/var/mongodb-rs/log"
config_path: "/var/mongodb-rs/config"

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