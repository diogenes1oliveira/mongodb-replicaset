# mongo-deployment-role

Manages a MongoDB deployment.

## Requirements

Requires a YUM-capable system with MongoDB already installed and configured.

## Role Variables

```yaml
## defaults file for mongo-deployment-role

# Default root password from the AMI. Will be used to login in the first
# deployment.
default_root_password: "12345678"

# Root user password. Will be changed from the default password during
# the first deployment
root_password: null
```

```yaml
## vars file for mongo-deployment-role

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
    - role: mongo-deployment-role
      log_path: /var/mongodb/log
      run_path: /run/mongodb
```

## License

MIT

## Author Information

Diógenes Oliveira
diogenes1oliveira@gmail.com
