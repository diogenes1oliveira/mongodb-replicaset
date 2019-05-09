def keyfiles_are_valid(keyfiles, min_length=50):
    '''
    Checks if all the keyfiles are valid: i.e., all equal and with 
    the minimum length.
    '''
    return len(set(keyfiles)) == 1 and len(keyfiles[0]) > min_length

class FilterModule(object):
    '''
    custom jinja2 filters for working with MongoDB stuff
    '''

    def filters(self):
        return {
            'keyfiles_are_valid': keyfiles_are_valid,
        }
