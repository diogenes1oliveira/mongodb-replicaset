import json

def keyfiles_are_valid(keyfiles, min_length=50):
    '''
    Checks if all the keyfiles are valid: i.e., all equal and with 
    the minimum length.
    '''
    return len(set(keyfiles)) == 1 and len(keyfiles[0]) > min_length


def needs_to_initialize(hostvars, hosts=None, registered_stat='initialization_file'):
    '''
    Checks if the replica set needs to be initialized
    '''
    checksum = None

    for host, vars in hostvars.items():
        if hosts and (host not in hosts):
            continue
        stat = getattr(vars[registered_stat], 'stat', None)
        if stat:
            if checksum and stat['checksum'] != checksum:
                raise Exception('Unsynchronized initialization')
            else:
                return False
            checksum = stat['checksum']
    else:
        return True


def replica_set_members(groups, data_group, arbiter_group):
    hosts = []

    for host in groups[data_group]:
        hosts.append({
            '_id': len(hosts),
            'host': f'{host}:27017',
        })
    for host in groups[arbiter_group]:
        hosts.append({
            '_id': len(hosts),
            'host': f'{host}:27017',
            'arbiterOnly': True,
        })
    
    return hosts


class FilterModule(object):
    '''
    custom jinja2 filters for working with MongoDB stuff
    '''

    def filters(self):
        return {
            'keyfiles_are_valid': keyfiles_are_valid,
            'needs_to_initialize': needs_to_initialize,
            'replica_set_members': replica_set_members,
        }
