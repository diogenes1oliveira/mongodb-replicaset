# mongo-baking-role

Bakes a MongoDB-ready AMI.

## Requirements

Currently, it only works on base systems that use the YUM package manager.

## Role Variables

```yaml
## default variables (defaults/main.yml)

# Path to the data directory
db_path: "/var/mongodb-rs/data"

# Path to the runtime data directory
run_path: "/var/mongodb-rs/run"

# Path to the log directory
log_path: "/var/mongodb-rs/log"

# Path to the config directory
config_path: "/var/mongodb-rs/config"

# TCP port to bind to when in no-auth mode
tcp_port_no_auth: 27020

# Name of the replica set to be deployed.
# In case this is falsey (default), standalone instances are deployed.
replica_set_name: null

# Sample password to be baked into the AMI (required).
root_password: null
```

```yaml
## default variables (defaults/main.yml)

# Run commands as root
ansible_become: true
```

## How to use it

Install and prepare Mongo in the instances:

```yaml
- hosts: servers
  roles:
    - role: "mongo-bootstrapping-role"
      root_password: < YOUR ROOT PASSWORD HERE >
```

## License

MIT

## Author Information

Diógenes Oliveira
diogenes1oliveira@gmail.com
