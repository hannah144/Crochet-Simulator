import json

################################################################################
class Yarn:
    '''Yarn is a basic data type used to create a Stitch.'''
    names = []
    yarn_dict = {}
    isw = {
        '0 - Lace' : {'low' : 600, 'high' : 10000},
        '1 - Super Fine' : {'low' : 350, 'high' : 600},
        '2 - Fine' : {'low' : 250, 'high' : 350},
        '3 - Light' : {'low' : 200, 'high' : 250},
        '4 - Medium' : {'low' : 120, 'high' : 200},
        '5 - Bulky' : {'low' : 100, 'high' : 120},
        '6 - Super Bulky' : {'low' : 0, 'high' : 100}
        } # isw = international standard weights

    def __init__(self, name = '', info = {}):
        '''Main constructor. See class doc string.'''
        if name != '':
            self.name = info['name']['ans']
            self.short_name = info['short_name']['ans']
            self.yardage = info['yardage']['ans']
            self.weight = info['weight']['ans']
            self.wei = self.calc_weight()
            self.thickness = self.weight/self.yardage
            self.composition = info['composition']['ans']
            self.care = info['care']['ans']
            self.info = info

            Yarn.yarn_dict[name.title()] = self
            Yarn.names.append(name.title())

#   ~~ additional constructors ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @classmethod
    def generate_defaults(cls):
        '''Constructs prebuilt yarn instances saved in yarn.json.'''
        with open('yarn.json') as f:
            data = json.load(f)
            new_yarns = data['yarns']

            for yarn in new_yarns.keys():
                Yarn(yarn,new_yarns[yarn])

    @classmethod
    def add_new_yarn(cls):
        '''Gets new yarn attributes from user to create and save a new
        yarn instance.
        '''
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        print('Please enter the following yarn info:\n') # Get attributes

        info = {"name" : {"ask" : "Full Name: "},
                "short_name" : {"ask" : "Short-Hand Name: "},
                "color" : {"ask" : "Color: "},
                "weight" : {"ask" : "Skien Weight(g): "},
                "yardage" : {"ask" : "Skien Yardage(yd): "},
                "composition" : {"ask" : "Yarn Composition: "},
                "care" : {"ask" : "Care Instructions: "}}

        for i in info.keys():
            while True:
                ans = input(info[i]['ask'])
                if i == 'weight' or i  == 'yardage':
                    try:
                        ans = float(ans)
                        break
                    except:
                        print('Must be an int or float value')
                else:
                    break
            info[i]['ans'] = ans

        with open('yarn.json','r+') as f: # save yarn instance
            data = json.load(f)
            data['yarns'].update({info['name']['ans'] : info})
            f.seek(0)
            json.dump(data, f)

        Yarn(info['name']['ans'], info) # instantiate yarn instance
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#   ~~ attribute calculations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def calc_weight(self):
        '''Returns the weight class of yarn instance, based on the
        international standard weights of the craft yarn council.
        '''
        m_g = ((self.yardage * 0.9144) * 100)/self.weight
        for k in Yarn.isw.keys():
            if m_g > Yarn.isw[k]['low'] and m_g < Yarn.isw[k]['high']:
                return k

#   ~~ mutators ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @classmethod
    def select_yarn_list(cls):
        '''Returns a numbered list of yarns in inventory.'''
        names = Yarn.names
        rng = range(len(names))

        yarn_lists = ['(' + str(i+1) + ') ' + names[i] for i in rng]
        yarn_list = '\n'.join(yarn_lists)
        return yarn_list

    def get_info(self):
        '''Returns a formated string of a yarn's attributes.'''
        info_strng =  ''
        for k in self.info.keys():
            info_strng += self.info[k]['ask'] + str(self.info[k]['ans']) + '\n'
        return  info_strng

#   ~~ magic methods ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def  __repr__(self):
        '''Returns formated name of yarn instance.'''
        return self.name.title()
    
    def __str__(self):
        '''Returns formated name of yarn instance.'''
        return self.name.title()
