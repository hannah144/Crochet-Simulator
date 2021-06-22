from stitch_type import Stitch_Type
from yarn import Yarn
from hook import Hook
from stitch import Stitch
from row import Row
from gaugesq import GaugeSq
from pattern  import Pattern
import json
import sys

class Interface():
    '''Allows user to interact with classes.'''
    def __init__(self):
        '''Main constructor. See class doc string.'''
        self.menus = {}
        self.load_menus()

        Yarn.generate_defaults()
        Stitch_Type.generate_defaults()
        Stitch.generate_defaults()
        Row.generate_defaults()
        Pattern.generate_defaults()

        self.yarns =  Yarn.yarn_dict
        self.hooks = Hook.hooks
        self.stitch_types = Stitch_Type.stitch_types
        self.stitches = Stitch.stitches
        self.rows = Row.rows
        self.patterns = Pattern.patterns

        print(self.menus['welcome'])
        self.main_menu()

#   ~~ additional constructors ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def load_menus(self):
        '''Loads prebuilt menu dictionary saved in menu.json.'''
        with open('menus.json') as f:
            data = json.load(f)
            self.menus = data['menus']

#   ~~ menu methods ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def main_menu(self):
        '''Prints main menu of program & allows user access classes.'''
        while True:
            print(self.menus['main_menu'])
            menu_opt = [7,'exit']
            ans = self.input_checker(menu_opt)

            if ans ==  1:
                self.yarn_menu()
            elif  ans == 2:
                self.print_hooks()
            elif ans == 3:
                self.stitch_type_menu()
            elif ans == 4:
                self.stitch_menu()
            elif ans == 5:
                self.gaugesq_menu()
            elif ans == 6:
                self.row_menu()
            elif ans == 7:
                self.pattern_menu()
            elif ans == 'exit':
                print('Goodbye!')
                sys.exit()

    def yarn_menu(self):
        '''Prints main yarn menu of program & allows user access Yarn
        class instances.
        '''
        while True:
            yarns = Yarn.select_yarn_list()
            print(self.menus['yarn_menu'].format(list_yarns = yarns))

            menu_opt = [len(Yarn.names),'add','q']
            ans = self.input_checker(menu_opt)
            if ans == 'q':
                break
            elif ans == 'add':
                Yarn.add_new_yarn()
            else:
                yarn = Yarn.yarn_dict[Yarn.names[ans-1]]
                self.print_yarn_info(yarn)

    def print_yarn_info(self, yarn):
        '''Nicely prints yarn instance attributes for easy viewing.'''
        while True:
            info_string = yarn.get_info()
            print(self.menus['yarn_info'].format(
                name = yarn.name,
                info =  info_string))

            menu_opt = [0,'q']
            ans = self.input_checker(menu_opt)

            if ans == 'q':
                break

    def print_hooks(self):
        '''Nicely prints hook instances for easy viewing.'''
        while True:
            hook_list = Hook.get_hook_list()
            print(self.menus['hook_list'].format(hook_list = hook_list))

            menu_opt = [0,'q']
            ans = self.input_checker(menu_opt)

            if ans == 'q':
                break

    def stitch_type_menu(self):
        '''Prints main stitch type menu of program & allows user access
        Stitch_Type class instances.
        '''
        while True:
            stitch_types = Stitch_Type.select_stitch_type()
            print(self.menus['stitch_type_menu'].format(
                stitch_types = stitch_types))

            menu_opt = [len(Stitch_Type.names),'q']
            ans = self.input_checker(menu_opt)

            if ans == 'q':
                break
            else:
                stitch_type = Stitch_Type.stitch_types[Stitch_Type.names[ans - 1]]
                self.print_stitch_views(stitch_type)

    def print_stitch_views(self, st):
        '''Nicely prints side view of a stitch type.'''
        while True:
            name = st.name + ' [' + st.abrv + ']'
            view = st.vis_rep()
            print(self.menus['stitch_type_views'].format(
                name = name,
                views = view))

            menu_opt = [0,'q']
            ans = self.input_checker(menu_opt)

            if ans == 'q':
                break

    def stitch_menu(self):
        '''Prints main stitch menu of program & allows user access and
        create Stitch_Type class instances.
        '''
        while True:
            stitch_list = Stitch.select_stitch()
            print(self.menus['stitch_menu'].format(stitch_list = stitch_list))

            menu_opt = [len(Stitch.stitches),'add','q']
            ans = self.input_checker(menu_opt)

            if ans == 'q':
                break
            elif ans == 'add':
                self.add_stitch_menu()
            else:
                stitch = Stitch.stitches[Stitch.names[ans-1]]
                self.stitch_info(stitch)

    def stitch_info(self, st):
        '''Nicely prints stitch instance attributes and visual
        representation for easy viewing.
        '''
        while True:
            name = st.name
            info = st.get_stitch_info()
            view = st.stitch_type.vis_rep()
            print(self.menus['stitch_view'].format(
                name = name,
                info = info,
                view =  view))

            menu_opt = [0,'q']
            ans = self.input_checker(menu_opt)

            if ans == 'q':
                break

    def add_stitch_menu(self):
        '''Allows user to build and save a new stitch'''
        stitch_name = input('Enter new stitch name: ')

        #set default attributes:
        yarn = Yarn.yarn_dict['Red Heart Super Saver - Aruba Sea']
        hook = Hook(6.0)
        stitch_type = Stitch_Type.stitch_types['Single Crochet']

        while True:
            attribute_txt = '''
(1) Yarn: {yarn}
(2) Hook: {hook}
(3) Stitch Type: {stitch_type}
'''
            attributes = attribute_txt.format(
                yarn = yarn.name,
                hook = hook,
                stitch_type = stitch_type.name)
            print(self.menus['add_stitch_menu'].format(
                name = stitch_name,
                stitch_attributes = attributes))

            menu_opt = [3,'save','q']
            ans = self.input_checker(menu_opt)

            if ans == 'q':
                break
            elif ans == 'save': # creates Stitch instance & saves to stitch.json
                info = {"name" : stitch_name,
                        "yarn" : yarn.name,
                        "hook" : hook.name,
                        "stitch_type" : stitch_type.name}
                st = Stitch(stitch_name, info)
                st.save_stitch()
                print(stitch_name, '- saved!')
                break
            elif ans ==  1: # change yarn
                yarn = self.select_yarn(stitch_name, yarn)
            elif ans  == 2: # change hook size
                hook = self.select_hook(stitch_name, hook)
            elif ans ==  3: # change stitch type
                stitch_type = self.select_stitch_type(stitch_name, stitch_type)

    def select_yarn(self, stitch_name, og_yarn):
        '''Allows user to select yarn for their new stitch'''
        while True:
            yarn_list = Yarn.select_yarn_list()
            print(self.menus['select_yarn'].format(
                name = stitch_name,
                yarn_list = yarn_list))

            menu_opt = [len(Yarn.names),'q']
            ans = self.input_checker(menu_opt)

            if ans == 'q':
                return og_yarn
            else:
                return Yarn.yarn_dict[Yarn.names[ans-1]]

    def select_hook(self, stitch_name, og_hook):
        '''Allows user to select a hook for their new stitch'''
        print(self.menus['select_hook'].format(
                name = stitch_name))
        while  True:
            flt =  input(': ')
            if flt == 'q':
                break
            try:
                return Hook(float(flt))
            except:
                print('Oops! Enter a float please (like a decimal value)')
                continue

    def select_stitch_type(self, stitch_name, og_stitch_type):
        '''Allows user to select a stitch_type for their new stitch'''
        while True:
            stitch_type_list = Stitch_Type.select_stitch_type()
            print(self.menus['select_stitch_type'].format(
                name = stitch_name,
                stitch_type_list = stitch_type_list))

            menu_opt = [len(Stitch_Type.names),'q']
            ans = self.input_checker(menu_opt)

            if ans == 'q':
                return og_stitch_type
            else:
                return Stitch_Type.stitch_types[Stitch_Type.names[ans-1]]

    def row_menu(self):
        '''Prints main row menu of program & allows user access and
        create Row class instances.
        '''
        while True:
            row_list = Row.select_row(boo = True)
            print(self.menus['row_menu'].format(row_list = row_list))

            menu_opt = [len(Row.names),'add', 'q']
            ans = self.input_checker(menu_opt)

            if ans ==  'q':
                break
            elif ans == 'add':
                self.add_new_row()
            else:
                row = Row.rows[Row.names[ans-1]]
                self.get_row_info(row)

    def get_row_info(self,row):
        '''Nicely prints row instance attributes for easy viewing.'''
        while True:

            stitch_list =''
            for k in row.stitch_values.keys():
                stitch_values = row.stitch_values[k]
                name = stitch_values['name']
                attributes = stitch_values['value'].pretty_stitch_attributes()
                stitch_list += '(' + k + ') ' + name + '\n' + attributes
            row_pattern = row.row_pattern
            height = row.height
            width = row.width
            weight = row.weight
            print(self.menus['row_info'].format(
                row_name = row.name,
                row_pattern = row_pattern,
                list_stitches_n_info = stitch_list,
                height = '%.4f' %height + 'in',
                width = '%.4f' %width + 'in',
                weight = weight))

            menu_opt = [0,'rep','add', 'quit']
            for k in row.stitch_values.keys():
                menu_opt.append(k)
            ans = self.input_checker(menu_opt)

            if ans == 'quit':
                break
            elif ans in row.stitch_values.keys():
                self.stitch_info(row.stitch_values[ans]['value'])
            elif ans  == 'rep':
                self.get_row_view(row)

    def get_row_view(self, row):
        '''Nicely prints side view of row instance.'''
        while True:
            name = row.name
            view = row.print_row()
            print(self.menus['row_view'].format(
                name = name,
                side_view = view))

            menu_opt = [0,'q']
            ans = self.input_checker(menu_opt)

            if ans  == 'q':
                break

    def add_new_row(self):
        '''Allows user to build and save a new row.'''
        name = input('Enter new row name: ')

        ans = self.select_row_stitches() # ask user to select stitches for row

        if ans == 'q':
            return

        while True: # ask user for row pattern
            stitch_list = ''
            for k in ans.keys():
                stitch_list += '(' + k + ') ' + ans[k]['name'] + '\n'
            print(self.menus['add_new_row'].format(
                name = name,
                stitch_list = stitch_list))

            usr_inpt = input(': ')
            if usr_inpt.lower() ==  'quit':
                break
            if usr_inpt.lower() == 'help':
                Row.row_pattern_help()
            else:
                r = Row(name, ans, usr_inpt)
            if name in Row.names:
                r.save_row()
                break

    def select_row_stitches(self):
        '''Allows user to select stitches for new row.'''
        while True:
            stitch_list  = Stitch.select_stitch()
            print(self.menus['select_row_stitches'].format(
                stitch_list = stitch_list))

            menu_opt = [len(Stitch.names),'q']
            ans = self.input_checker(menu_opt,rng = True)
            return ans

    def gaugesq_menu(self):
        '''Prints main gauge square menu of program & allows user to
        create Gauge Square class instances.
        '''
        while True:
            stitch_list = Stitch.select_stitch()
            print(self.menus['add_gaugesq'].format(
                stitch_list=stitch_list))

            menu_opt = [len(Stitch.names),'add','q']
            ans = self.input_checker(menu_opt)

            if ans == 'q':
                break
            elif ans == 'add':
                self.add_stitch_menu()
            else:
                st = self.stitches[Stitch.names[ans-1]]
                gs = GaugeSq(st)
                self.gaugesq_info(gs)

    def gaugesq_info(self, gs):
        '''Nicely prints gauge square instance attributes for easy
        viewing.
        '''
        while True:
            name = gs.stitch.name
            info = gs.get_info()
            print(self.menus['gaugesq_info'].format(
                stitch_name = name,
                info = info))

            menu_opt = [0,'rep','q']
            ans = self.input_checker(menu_opt)

            if ans == 'q':
                break
            if ans == 'rep':
                self.gaugesq_view(gs)

    def gaugesq_view(self, gs):
        '''Nicely prints side view of gauge square instance.'''
        while True:
            name = gs.stitch.name
            view = gs.get_view()
            print(self.menus['gaugesq_view'].format(
                stitch_name = name,
                view = view))

            menu_opt = [0,'q']
            ans = self.input_checker(menu_opt)

            if ans == 'q':
                break

    def pattern_menu(self):
        '''Prints main pattern menu of program & allows user to
        create pattern class instances.
        '''
        while True:
            pattern_list = Pattern.select_pattern()
            print(self.menus['pattern_menu'].format(
                pattern_list = pattern_list))

            menu_opt = [len(Pattern.names), 'add', 'q']
            ans = self.input_checker(menu_opt)

            if ans == 'q':
                break
            elif ans == 'add':
                self.add_pattern()
            else:
                pattern = Pattern.patterns[Pattern.names[ans-1]]
                self.pattern_info(pattern)

    def pattern_info(self, pattern):
        '''Nicely prints pattern instance attributes for easy
        viewing.
        '''
        while True:
            name = pattern.name
            sequence = pattern.sequence
            metrics =  pattern.get_metrics()
            row_list = ''
            for k in pattern.row_values.keys():
                row_list += '(' + k + ') ' + pattern.row_values[k]['name'] + '\n'
            print(self.menus['pattern_info'].format(
                name = name,
                sequence = sequence,
                list_rows = row_list,
                metrics = metrics))

            menu_opt = [0,'rep','quit']
            for k in pattern.row_values.keys():
                menu_opt.append(k)
            ans = self.input_checker(menu_opt)

            if ans == 'quit':
                break
            elif ans in pattern.row_values.keys():
                self.get_row_info(pattern.row_values[ans]['value'])
            elif ans  == 'rep':
                self.get_pattern_view(pattern)

    def get_pattern_view(self, pattern):
        '''Nicely prints side view of pattern instance.'''
        while True:
            name = pattern.name
            view = pattern.print_pattern()
            print(self.menus['pattern_view'].format(
                name = name,
                side_view = view))

            menu_opt = [0,'q']
            ans = self.input_checker(menu_opt)

            if ans  == 'q':
                break

    def add_pattern(self):
        '''Allows user to build and save a new pattern.'''
        name = input('Enter new pattern name: ')  # get New Pattern Name
        ans = self.select_pattern_rows() # ask user to select stitches for row
        if ans == 'q':
            return

        while True: # ask user for pattern sequence
            row_list = ''
            for k in ans.keys():
                row_list += '(' + k + ') ' + ans[k]['name'] + '\n'
            print(self.menus['add_pattern'].format(
                name = name,
                row_list = row_list))

            usr_inpt = input(': ')
            if usr_inpt.lower() ==  'quit':
                break
            if usr_inpt.lower() == 'help':
                Pattern.pattern_help()
            else:
                r = Pattern(name, ans, usr_inpt)
            if name in Pattern.names:
                r.save_pattern()
                break

    def select_pattern_rows(self):
        '''Asks user to select rows for pattern.'''
        while True:
            row_list  = Row.select_row()
            print(self.menus['select_pattern_rows'].format(
                list_rows = row_list))

            menu_opt = [len(Row.names),'q']
            ans = self.input_checker(menu_opt,pattern = True)

            if isinstance(ans, int):
                print('works')
                row = Row.rows[Row.names[ans-1]]
                self.get_row_info(row)
            else:
                return ans

    def input_checker(self, opt_inpt, rng = False, pattern =  False):
        '''Ensures valid user input.'''
        line = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        while True:
            usr_inpt = input(': ')

            try:
                num = int(usr_inpt)
            except:
                num = 0

            if rng == True:
                ans = Row.select_row_stitches(usr_inpt)
                if ans != 'error':
                    return  ans

            if pattern == True and num == 0:
                ans = Pattern.select_pattern_rows(usr_inpt)
                if ans != 'error':
                    return ans

            if num > 0 and num <= opt_inpt[0]:
                ans = num
                print(line)
                return ans
            elif usr_inpt.lower() in opt_inpt[1:]:
                ans = usr_inpt.lower()
                print(line)
                return ans
            else:
                print('Invalid Input!')
