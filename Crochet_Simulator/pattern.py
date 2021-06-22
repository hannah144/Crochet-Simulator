###############################################################################
from row import Row
import  copy
import json

class Pattern:
    '''A Pattern is a  list of  rows.'''
    patterns =  {}
    names =  []
    def __init__(self, name, rows, sequence):
        '''Main constructor. See class doc string.'''
        pattern_values = Pattern.evaluate_pattern(name, rows, sequence)
        if pattern_values == False:
            return
    
        self.pattern_values = pattern_values
        self.name = name
        self.rows = rows
        self.row_values = copy.deepcopy(rows)
        for k in rows.keys():
            entry = {'value' : Row.rows[rows[k]['name']]}
            self.row_values[k].update(entry)
        self.sequence = sequence

        self.height = self.calc_height()
        self.width  = self.calc_width()
        self.weight = self.calc_weight()
        
        Pattern.patterns[self.name] = self
        Pattern.names.append(self.name)

#   ~~ constructor ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @classmethod
    def generate_defaults(cls):
        '''Constructs prebuilt pattern instances saved in
        pattern.json.
        '''
        with open('pattern.json') as f:
            data = json.load(f)
            new_pattern = data['patterns']
            
            for p in new_pattern.keys():
                Pattern(p, new_pattern[p]['rows'], new_pattern[p]['sequence'])
                
    @classmethod
    def evaluate_pattern(cls, name, my_rows, sequence):
        '''Checks pattern sequence validity, if valid it will create a
        new pattern instance.
        '''
        operators = ['+','(',')','*']
        letters = [k for k in my_rows.keys()]
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        cool_vals =  operators + letters + numbers
        
        sequence = sequence.replace(' ','')
        pattern_exe =  '' 
        num = ''
        for x in list(sequence):
            if  x not in cool_vals:
                print('Error!')
                return False
            if x not in numbers:
                if num !='':
                    pattern_exe += num
                    num = ''

                if x in operators:
                    pattern_exe += x
                elif x in letters:
                     pattern_exe += "Row.rows['{row_name}']".format(
                        row_name =  my_rows[x]['name'])
            else:
                num += x
        if num != '':
            pattern_exe += num   
        try:
            pattern_values = eval(pattern_exe)
        except:
            print('Oops! Something\'s wrong with  your pattern. try again!')
            pattern_values = False
        return pattern_values
        
        
    @classmethod
    def select_pattern_rows(self, inpt):
        '''Returns dictionary that has alphabet keys for each row.'''
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        inpts = inpt.replace(' ','').split(',')
        my_rows = {}
        try:
            indices = [int(i) - 1 for i in inpts if i != '']
            row_lengths = []
            for i in range(len(indices)):
                r = Row.rows[Row.names[indices[i]]]
                row_lengths.append(r.length)
        except:
            return 'error'

        #check row compatibility
        if row_lengths[0] != sum(row_lengths)/len(indices):
            print('Oops! Your pattern\'s rows need to all be the same length!')
            return 'error'
                
        for i in range(len(indices)):
            alpha = alphabet[i]
            name = Row.names[indices[i]]
            new_entry = {alpha : {'name' : name}}
            my_rows.update(new_entry)
        return my_rows

#   ~~ attribute calculations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def calc_height(self):
        '''Returns max height of summed up row heights in pattern.'''
        heights = [0 for x in range(self.pattern_values[0].length)]
        for r in self.pattern_values:
            for h in range(len(heights)):
                heights[h] += r.row_values[h].height
        max_height = max(heights)
        return max_height
    
    def calc_width(self):
        '''Returns average row_width of rows in pattern.'''
        widths = [r.width for r in self.pattern_values]
        avg_width = sum(widths)/len(widths)
        return avg_width
    
    def calc_weight(self):
        '''Returns max stitch_weight of rows in pattern.'''
        weights = {r.weight[0] : r.weight for r in self.pattern_values}
        max_weight = weights[max(weights.keys())]
        return max_weight
    
#   ~~ mutators ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @classmethod
    def select_pattern(cls):
        '''Returns a list of numbered patterns.'''
        pattern_list = ''
        for i in range(len(Pattern.names)):
            p = Pattern.names[i]
            pattern_list += '(' + str(i+1) + ') ' + p + '\n'
        return pattern_list
    
    def get_metrics(self):
        'Returns nicely formatted pattern instance metrics.'''
        metrics = 'Height = ' + '%.4f' %self.height + 'in\n' \
                  + 'Width = ' + '%.4f' %self.width + 'in\n' \
                  + 'Weight = ' + self.weight
        return metrics
        
    def print_pattern(self):
        '''Returns a visual representation of pattern instance.'''
        pattern_view = ''
        for row in self.pattern_values:
            row_view = row.print_row()
            pattern_view = row_view + '\n' + pattern_view
        return pattern_view

    def save_pattern(self):
        '''Saves pattern to pattern.json.'''
        info = {"name" : self.name, "rows" : self.rows, "sequence" : self.sequence}
        with open('pattern.json','r+') as f:
            data = json.load(f)
            data['patterns'].update({info["name"]:info})
            f.seek(0)
            json.dump(data, f)
        print(self.name +  ' saved!')
    
    @classmethod    
    def pattern_help(cls):
        '''Prints a help message for users confused about building a
        new pattern instance.
        '''
        with open('help.json') as f:
            data = json.load(f)
            help_txt = data['help']
        print(help_txt['pattern_help'])
        inpt = input('Enter any key to return to add a new pattern: ')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
