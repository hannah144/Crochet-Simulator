from stitch import Stitch
from row import Row
import math

class GaugeSq:
    '''Generates a 4x4 inch gauge square using a single stitch. Methods
    help inform the user how many stitches and rows are needed to create
    a 4x4 inch crochet square.
    '''
    def __init__(self, stitch):
        '''Main constructor. See class doc string.'''
        self.stitch = stitch
        self.num_stitches = self.get_num_stitches()
        self.num_rows = self.get_num_rows()
        self.row = Row('', {'a':{'name':stitch.name}}, \
                       'a*' + str(self.num_stitches))

#   ~~ attribute calculations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_num_stitches(self):
        '''Returns number of stitches needed to reach 4 inches.'''
        st = self.stitch
        st_width = st.width *  0.393701
        num_stitches = math.ceil(4/st_width)
        return num_stitches

    def get_num_rows(self):
        '''Returns number of rows needed to reach 4 inches.'''
        st = self.stitch
        st_height = st.height *  0.393701
        num_rows = math.ceil(4/st_height)
        return num_rows

#   ~~ mutators ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_view(self):
        '''Returns visual representation of the gauge square in ascii.'''
        gaugesq_vis =  ''
        for x in range(self.num_rows):
            gaugesq_vis += self.row.print_row() + '\n'
        return gaugesq_vis

    def get_info(self):
        '''Returns formated information about gauge square.'''
        info = ''
        info += str(self.num_stitches) + ' Stitches needed to make 4in width\n'
        info += str(self.num_rows) + ' Rows needed to make 4in height\n'
        info += 'Weight : ' + self.row.weight
        return info
