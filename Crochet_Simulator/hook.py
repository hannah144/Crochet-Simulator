################################################################################
class Hook:
    '''A Hook is a basic data type used to create Stitches.'''
    hooks = {}
    def __init__(self, flt):
        '''Main constructor. See class doc string.'''
        self.name = str(flt)
        self.size = flt
        self.metric = 'mm'
        Hook.hooks[str(flt)] = self

#   ~~ mutators ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @classmethod
    def get_hook_list(cls):
        '''Returns a sorted list of recently generated hooks.'''
        hook_list = ''
        hooks_by_size = sorted([(h.size,h) for h in Hook.hooks.values()])
        for h in hooks_by_size:
            hook_list += h[1].name + '_mm\n'
        return hook_list

#   ~~ magic methods ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __repr__(self):
        '''Returns formated name of hook instance.'''
        return self.name + '_' + self.metric

    def __str__(self):
        '''Returns formated name of hook instance.'''
        return self.name + '_' + self.metric
