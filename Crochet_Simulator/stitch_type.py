import json

################################################################################
class Stitch_Type:
    '''The stitch type is a basic data type used to create a Stitch.'''
    stitch_types = {}
    names = []
    def __init__(self, name, info = {}):
        '''Main constructor. See class doc string.'''
        self.abrv = name
        self.name = info['name']
        self.side = info['side_view']
        self.top = info['top_view']
        self.yardage_cons = info['yardage_cons']
        self.height_cons = info['height_cons']
        self.info = info
        
        Stitch_Type.stitch_types[self.name] = self
        Stitch_Type.names.append(self.name)
        
#   ~~ constructors ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @classmethod
    def generate_defaults(cls):
        '''Constructs prebuilt stitch type instances saved in
        stitch_type.json.
        '''
        with open('stitch_type.json') as f:
            data = json.load(f)
            new_stitch_types = data['stitch_types']
            
            for stitch_type in new_stitch_types.keys():
                Stitch_Type(stitch_type,new_stitch_types[stitch_type])
            
#   ~~ mutators ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @classmethod
    def select_stitch_type(cls):
        '''Returns a numbered list of stitch types in inventory.'''
        stitch_type_list = []
        for i in range(len(Stitch_Type.names)):
            name = Stitch_Type.stitch_types[Stitch_Type.names[i]].name
            abrv = Stitch_Type.stitch_types[Stitch_Type.names[i]].abrv
            txt = '(' + str(i + 1) + ') ' + name + ' [' + abrv + ']'
            stitch_type_list.append(txt)
            
        stitch_type_list = '\n'.join(stitch_type_list)
        return stitch_type_list
    
    def vis_rep(self):
        '''Returns ascii representation of the stitch_type instance'''
        side_long = 'Side View:\n'
        for s in self.side[0:]:
            side_long += s + '\n'
        return side_long
    
#   ~~ magic methods ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __repr__(self):
        '''Returns formated name of stitch type instance.'''
        return self.name +  '['  + self.abrv + ']'
    
    def __str__(self):
        '''Returns formated name of stitch type instance.'''
        return self.name +  '['  + self.abrv + ']'
    
