"""
Pairs
- class to create pairs
PairSet
- class to create sets of pairs for user based on what is in preferances
"""
class Pairs:

    """
    Pairs
    - get_index_of_pair
    - get_pairs
    - get_dict_comparisions
    - is_pair
    - is_pair_equal
    """
    
    def __init__(self):
        self.index_a = []
        self.index_b = []
        self.index_ab =[]

        self.BASE_SIZE = 50                             # amount of items that will be compared 
        self.TOTAL_COM = self.BASE_SIZE*self.BASE_SIZE  # total amount of comparisions possible, including with each other, is pizza_index square
        # if pizza_index is 50 the max is 2500
        self.USER_COM = 109                              # total amount of comparisons users will make

    def set_total(self,size):
        self.BASE_SIZE = size
        self.TOTAL_COM = self.BASE_SIZE*self.BASE_SIZE

    def get_index_of_pair(self, left_pair, right_pair):
        # calculating the position a pair is in an index of pairs
        no_of_items_in_index = self.BASE_SIZE
        return (((left_pair * no_of_items_in_index) - no_of_items_in_index)) + right_pair
        
    def get_pairs(self, index_of_pair):
        # returns a pair from the index of all possible pairs in the set
        no_of_items_in_index = self.BASE_SIZE

        # roughly where the pair are in the index
        starting_point_of_pair_set_in_index = index_of_pair / no_of_items_in_index

        right_pair = index_of_pair - starting_point_of_pair_set_in_index * no_of_items_in_index

        if right_pair == no_of_items_in_index: left_pair = starting_point_of_pair_set_in_index
        else: left_pair = starting_point_of_pair_set_in_index + 1
        
        return left_pair, right_pair
    
    def is_pair(self, index_of_pair):
        if index_of_pair < self.TOTAL_COM: return True
        else: return False

    def is_pair_equal(self, index_of_pair):
        left_pair, right_pair = self.get_pairs(index_of_pair)
        if left_pair == right_pair: return True
        else: return False

    def get_dict_comparisions(self):
        # create a dictionary of non matching, orginal pairs
        dict_comparisions = { }

        for i in range(len(self.index_a)):
            # check pair doesn't exist
                pairs = self.get_index_of_pair(self.index_a[i], self.index_b[i])
                dict_comparisions[pairs] = 2 # value of not 0 or 1
                
        return dict_comparisions

class PairSet:
    """
    PairSet
    - set_index_size
    - set_first_pairs
    - is_pairset
    - get_comp_pairs
    - get_index
    - get_dict
    - get_first_dict
    - prep_pairs

    """

    def __init__(self):
        self.indexs = []
        self.lefts = []
        self.rights = []
        self.pairs = Pairs()
        self.SIZE = self.pairs.BASE_SIZE # size set to amount of pairs
        self.NUM_COMP = 10

    def set_index_size(self, size):
        # sets indexs size with pair object
        # if reset when user has already made choices from pairs this would have to be reset
        self.pairs.set_total(size)
        self.SIZE = self.pairs.BASE_SIZE

    def set_first_pairs(self):
        # creates pairs based on the x ranking pair set
        lefts = [x for x in range(1,self.SIZE + 1)]
        rights = [x for x in range(1,self.SIZE + 1)]
        r = rights.pop(0)
        rights.append(r)
        indexs=[]
        for i in range(0,len(lefts)):
            indexs.append(self.pairs.get_index_of_pair(lefts[i],rights[i]))
        return lefts, rights, indexs

    def is_pairset(self, index_of_pair):
        if self.pairs.is_pair(index_of_pair):
            return True
        else:
            False

    def get_comp_pairs(self, start):
        indexs = self.get_index(start)
        lefts = []
        rights = []

        for i in range(0,len(indexs)):
            left, right = self.pairs.get_pairs(indexs[i])
            lefts.append(left)
            rights.append(right)
        return lefts, rights, indexs

    def get_index(self, start):
        # Returns a valid index        
        indexs = [x for x in range(start, start+self.NUM_COMP+ 1)]
        new_indexs = [x for x in range(start, start+self.NUM_COMP+ 1)]
        for i in range(0,len(indexs)):
            # check index of pair is in set and not equal
            if self.pairs.is_pair(indexs[i]):
                if self.pairs.is_pair_equal(indexs[i]): new_indexs.remove( indexs[i] )
            else: new_indexs.remove( indexs[i] )
        return new_indexs

    def get_dict(self, start_index):
        # Catches if index if good to use
        if self.is_pairset(start_index):
            lefts, rights, indexs = self.get_comp_pairs(start_index)
            return {'lefts':lefts, 'rights': rights, 'indexs': indexs }
        else: return {'lefts':[0], 'rights': [0], 'indexs': [0] }

    def get_first_dict(self):
        lefts, rights, indexs = self.set_first_pairs()
        return {'lefts':lefts, 'rights': rights, 'indexs': indexs }

    def prep_pairs(self, p):
        x = {   'index' : p.index,
                'value': p.value,
                'time': p.time,
                'browser': p.browser,
                'b_h' : p.scrn_h,
                'b_w' : p.scrn_w,
                'scr_x': p.scroll_x,
                'scr_y': p.scroll_y,
                't_at' : p.t_at,
                'date' : str(p.date),
                'exp' : p.exp_no,
                'pic' : p.pic,
                'u_index':p.u_index,
                 }
        return x