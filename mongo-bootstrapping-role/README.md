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

  # password for the super user (required)
  admin_password: null

  replica_set: rs0     # name for the replica set
```

```yaml
# vars/main.yml
  # names of the groups for each role in the replica set
  data_group: 'data'
  arbiter_group: 'arbiter'

```


How to use it
-------------

Install and prepare Mongo in the instances:

    - hosts: servers
      roles:
        - role: 'mongo-bootstrapping-role'
          admin_password: < YOUR ROOT PASSWORD HERE >


License
-------

MIT

Author Information
------------------

Diógenes Oliveira
diogenes1oliveira@gmail.com