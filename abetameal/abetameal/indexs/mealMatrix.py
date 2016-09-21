# Meal Matrix to help create datbase and ML predictions
class MealMatrix:
    
    def __init__(self):
        self.Bredth=0
        self.Depth=0
        
    def set_size(self, bredth, depth):
        # Creates a n amount of meals by m amount of toppings matrix
        self.Depth = depth # meal amount
        self.Bredth = bredth # amount of toppings
        self.Matrix = [[0 for x in range(bredth)]for y in range(depth)]
    
    def has_meal(self, meal_index):
        # checks if the the size of matrix has will contain the index number of existing meal
        if (meal_index > self.Depth): return False
        else: return True
    
    def has_ing(self, meal_index, ingrd_indx):
        # see's if ingredients in meal index is set to 1
        if self.Matrix[meal_index][ingrd_indx] == 1: return True
        else: return False
    
    def add_ing(self, meal_index, ingrd_indx):
        # Takes in meal index number and ingredients index number sets ingredient to 1
        self.Matrix[meal_index][ingrd_indx] = 1
    
    def get_num_ing(self, meal_index):
        # Passing a meals index number will return the amount of ingredients it has
        count = 0
        for i in range(self.Bredth):
            if self.Matrix[meal_index][i] == 1:
                count = count + 1
        return count
        
    def get_ingr(self, meal_index):
        # given a meal index return array ingrdients
        ingrdients = []
        if self.contains_meal(meal_index):            
            for i in range(self.Bredth):
                if self.Matrix[meal_index][i] == 1:
                    ingrdients.append(i)        
        print 'meal_index: ', meal_index, 'ingrdients are', ingrdients
        return ingrdients

    def contains_meal(self, meal_index):
        # check meal is in list
        if meal_index > self.Depth:
            return False
        else:
            return True
            
    def __unicode__(self):
	    return self.Matrix