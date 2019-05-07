# mongo-log-rotation-role

Sets up logrotate for the log files of MongoDB.

## Requirements

Requires a YUM-capable system with MongoDB already installed and configured.

## Role Variables

```yaml
## defaults file for mongo-log-rotation-role

# Path to MongoDB log folder
log_path: /var/log/mongodb

# Path to MongoDB runtime folder
pid_path: /var/run/mongodb

# Maximum log file size
log_size: 100M
```

```yaml
## vars file for mongo-log-rotation-role

# Run the commands as root
ansible_become: true
```

## Dependencies

MongoDB must already be available and running, preferably via the role
`mongo-baking-role`.

## Example Playbook

Apply this role overriding the directories you want to customize:

```yaml
- hosts: servers
  roles:
    - role: mongo-log-rotation-role
      log_path: /var/mongodb/log
      run_path: /run/mongodb
```

## License

MIT

## Author Information

Diógenes Oliveira
diogenes1oliveira@gmail.com
