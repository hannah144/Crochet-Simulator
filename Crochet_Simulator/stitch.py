################################################################################
from stitch_type import Stitch_Type
from yarn import Yarn
from hook import Hook
import json

class Stitch:
    '''A stitch is comprised of a stitch type, yarn and hook size.'''
    stitches = {}
    names = []
    def __init__(self, name = '', info = {}):
        '''Main constructor. See class doc string.'''
        self.name = name
        self.stitch_type = Stitch_Type.stitch_types[info['stitch_type']]
        self.yarn = Yarn.yarn_dict[info['yarn']]
        self.hook = Hook(float(info['hook']))
        self.side = self.stitch_type.side
        self.info = info

        self.yarn_per_stitch = self.calc_yarn_per_stitch()
        self.height = self.calc_height()
        self.width = self.calc_width()
        self.weight =  self.yarn.wei

        Stitch.names.append(name)
        Stitch.stitches[name] = self

#   ~~ constructors ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @classmethod
    def generate_defaults(cls):
        '''Constructs prebuilt yarn instances saved in stitch.json.'''
        with open('stitch.json') as f:
            data = json.load(f)
            new_stitch = data['stitches']

            for st in new_stitch.keys():
                Stitch(st,new_stitch[st])
                
#   ~~ attribute calculations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def calc_yarn_per_stitch(self):
        '''Returns amt of yarn yardage need for stitch.'''
        constant = 5.721
        hook_constant = 1.240
        hook_size = self.hook.size
        stitch_constant =  self.stitch_type.yardage_cons

        if stitch_constant == 'None':
            return 0
        else:
            yardage = (0.393701
                       * (constant
                       + (hook_constant * hook_size)
                       + stitch_constant))
            return yardage

    def calc_height(self):
        '''Returns height of stitch.'''
        constant = .421
        hook_constant = .21
        hook_size = self.hook.size
        stitch_constant = self.stitch_type.height_cons

        if stitch_constant == 'None':
            return 0
        else:
            height = (0.393701
                      * (constant
                      + (hook_constant * hook_size)
                      + stitch_constant))
            return height

    def calc_width(self):
        '''Returns width of stitch.'''
        constant =  0.320
        hook_constant = .105
        hook_size = self.hook.size

        width = (0.393701
                 * (constant +
                 (hook_constant * hook_size)))
        return width
    
#   ~~ mutators ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @classmethod
    def select_stitch(cls):
        '''Returns a list of numbered stitches and their yarn, hook,
        and stitch type attributes.
        '''
        stitch_list = ''
        for i in range(len(Stitch.names)):
            st = Stitch.names[i]
            attributes = Stitch.stitches[st].pretty_stitch_attributes()
            stitch_list += '(' + str(i+1) + ') ' + st + '\n' + attributes
        return stitch_list

    @classmethod
    def build_row_stitch(cls):
        '''Returns a list of stitches numbered by letters, the letters
        are used for inputing the user's row pattern.
        '''
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        stitch_list = ''
        for i in range(len(Stitch.names)):
            st = Stitch.names[i]
            attributes = Stitch.stitches[st].pretty_stitch_attributes()
            stitch_list += '(' + alphabet[i] + ') ' + st + '\n' + attributes
        return stitch_list

    def pretty_stitch_attributes(self):
        '''Returns a nicely indented string of a stitch instance's yarn,
        hook and stitch type attributes.
        '''
        pretty_str = '    {abrv} -  {name} - {hook}\n'.format(
            abrv = self.stitch_type.abrv,
            name = self.yarn.short_name,
            hook = str(self.hook))
        return pretty_str

    def get_stitch_info(self):
        '''Returns formatted a stitch instance attribute information.'''

        general_attributes = self.pretty_stitch_attributes()
        height = '%.4f' %self.height + 'in'
        width = '%.4f' %self.width + 'in'
        weight = self.weight
        yardage = '%.4f' %self.yarn_per_stitch + 'in'

        info_strng = '''{attributes}
Height = {height}
Width = {width}
Weight = {weight}
Yardage per Stitch = {yardage}
'''
        info_strng = info_strng.format(
            attributes =  general_attributes,
            height = height,
            width = width,
            weight = weight,
            yardage  = yardage)
        return info_strng

    def save_stitch(self):
        '''Saves stitch to stitch.json.'''
        with open('stitch.json','r+') as f:
            data = json.load(f)
            data['stitches'].update({self.info["name"]:self.info})
            f.seek(0)
            json.dump(data, f)
            
#   ~~ magic methods ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __repr__(self):
        '''Returns formated name of stitch instance.'''
        return self.name.title()

    def __add__(self, other):
        '''Adds stitches by returning a list of those stitches.'''
        if isinstance(other,Stitch) == False and isinstance(other,list) == False:
            print('Oops! can only add a stitch to another stitch!')
            return False
        if isinstance(other,list) == True and isinstance(other[0],Stitch):
            stitch_list = [self]  +  other
        else:
            stitch_list = [self, other]
        return stitch_list

    def __mul__(self, other):
        '''Multiplies stitches by an int to return a list of stitches.'''
        if isinstance(other,int) == False:
            print('Oops! can only multiply a stitch by an int!')
            return False
        stitch_list  = [self for i in range(other)]
        return stitch_list
