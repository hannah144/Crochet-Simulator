###############################################################################

import json
from stitch import Stitch
import copy
class Row:
    '''A Row is a list of stitches.'''
    rows = {} 
    names = []
    def __init__(self, name, stitches, row_pattern):
        '''Main constructor. See class doc string.'''
        row_values = Row.evaluate_row_pattern(name, stitches, row_pattern)
        if  row_values == False:
            return None
        self.row_values = row_values #row values is a list of stitches
        self.name = name
        self.row_pattern = row_pattern
        self.stitches = stitches
        self.stitch_values = copy.deepcopy(stitches)
        for k in stitches.keys():
            entry = {'value' : Stitch.stitches[stitches[k]['name']]}
            self.stitch_values[k].update(entry)

        self.height = self.calc_height()
        self.width = self.calc_width()
        self.weight = self.calc_weight()
        self.length  = len(self.row_values)
        
        if name != '':
            Row.rows[name] = self
            Row.names.append(name)
        
#   ~~ constructors ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @classmethod
    def generate_defaults(cls):
        '''Constructs prebuilt row instances saved in row.json.'''
        with open('row.json') as f:
            data = json.load(f)
            new_row = data['rows']
            
            for r in new_row.keys():
                Row(r, new_row[r]['stitches'], new_row[r]['row_pattern'])
        
    @classmethod 
    def evaluate_row_pattern(cls, name, my_stitches, row_pattern):
        '''Checks row pattern validity, if valid it will create a new
        row instance.
        '''
        operators = ['+','(',')','*']
        letters = [k for k in my_stitches.keys()]
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        cool_vals =  operators + letters + numbers

        row_pattern = row_pattern.replace(' ','')
        row_pattern_exe =  '' 
        num = ''
        for x in list(row_pattern):
            if  x not in cool_vals:
                print('Error!')
                return False
            
            if x not in numbers:
                if num !='':
                    row_pattern_exe += num
                    num = ''
                if x in operators:
                    row_pattern_exe += x
                elif x in letters:
                    txt = 'Stitch.stitches[\'{stitch_name}\']'
                    row_pattern_exe += txt.format(
                        stitch_name = my_stitches[x]['name'])
            else:
                num += x
        if num != '':
            row_pattern_exe += num
        try:
            row_values = eval(row_pattern_exe)
        except:
            print('Oops! Something\'s wrong with your row pattern. Try again!')
            row_values = False
         
        return row_values

    @classmethod
    def select_row_stitches(self, inpt):
        '''Returns dictionary that has alphabet keys for each stitch.'''
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        inpts = inpt.replace(' ','').split(',')
        my_stitches = {}
        try:
            indices = [int(i) - 1 for i in inpts if i != '']
            for i in range(len(indices)):
                alpha = alphabet[i]
                name = Stitch.names[indices[i]]
                new_entry = {alpha : {'name' : name}}
                my_stitches.update(new_entry)
            return my_stitches
        except:
            return 'error'
        
#   ~~~~~~ attribute calculations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def calc_height(self):
        '''Returns max stitch height of stitches in row instance.'''
        max_height = max([st.height for st in self.row_values])
        return max_height
    
    def calc_width(self):
        '''Returns sum widths of stitches in row instance.'''
        sum_width = sum([st.width for st in self.row_values])
        return sum_width
    
    def calc_weight(self):
        '''returns max stitch_weight of stitches in row instance.'''
        i = 0
        max_weight = ''
        for k in self.stitch_values.keys():
            weight = self.stitch_values[k]['value'].weight
            w = weight[0]
            if int(w) > i:
                i = int(w)
                max_weight = weight
        return max_weight
    
#   ~~ mutators ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @classmethod
    def select_row(cls, boo = False):
        '''Returns a list of numbered rows.'''
        row_list = ''
        for i in range(len(Row.names)):
            r = Row.names[i]
            row_strng = '(' + str(i+1) + ') ' + r
            if boo == True:
                row_list += row_strng + '\n'
            else:
                length = Row.rows[r].length
                row_list += row_strng + '  len = ' + str(length) + '\n'
        return row_list
    
    def print_row(self):
        '''Returns a visual representation of row instance.'''
        row_vis =  []
        stitches = self.row_values
        stitch_sides = [st.side for st in stitches]
        
        max_stitch_len = max([len(st.side) for st in stitches])

        # ensures all stitch sides have equal # of elements
        for st in stitch_sides:
            while len(st) < max_stitch_len:
                st.insert(0, '   ')

        #concats stitch sides
        for i in range(max_stitch_len):
            line = []
            for v in range(len(stitches)):
                line.append(stitches[v].side[i])
            row_vis.append(''.join(line))
        row_vis = '\n'.join(row_vis)
        return row_vis

    def save_row(self):
        '''Saves row to row.json.'''
        info = {"name" : self.name,
                "stitches" : self.stitches,
                "row_pattern" : self.row_pattern}
        with open('row.json','r+') as f:
            data = json.load(f)
            data['rows'].update({info["name"]:info})
            f.seek(0)
            json.dump(data, f)
        print(self.name +  ' saved!')

    @classmethod
    def row_pattern_help(cls):
        '''Prints a help message for users confused about building a
        new row instance.
        '''
        with open('help.json') as f:
            data = json.load(f)
            help_txt = data['help']
        print(help_txt['row_help'])
        inpt = input('Enter any key to return to add a new row: ')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#   ~~ magic methods ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __repr__(self):
        '''Returns formated name of row instance.'''
        return self.name.title()

    def __add__(self, other):
        '''Adds rows by returning a list of those rows.'''
        if isinstance(other,Row) == False and isinstance(other,list) == False:
            print('Oops! can only add a row to another row or a list of rows!')
            return False
        if isinstance(other,list) == True and isinstance(other[0],Row):
            row_list = [self]  +  other
        else:
            row_list = [self, other]
        return row_list

    
    def __mul__(self, other):
        '''Multiplies rows by an int to return a list of rows.'''
        if isinstance(other,int) == False:
            print('Oops! can only multiply a row by an int!')
            return False
        row_list  = [self for i in range(other)]
        return row_list
