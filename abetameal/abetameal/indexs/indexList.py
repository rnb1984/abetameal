# Class to create an index list of Pizzas or ingredients that can only have one existance of any item
class IndexList:
    
    def __init__(self):
        self.index_list = []
        
    def un_plural(self, item):
        # Checks the item is not a plural of an existing item
        for i in self.index_list:
            if item == i + 's':
                return i
            if i == item + 's':
                # replcae if the existing ingredients is plural
                self.index_list[self.get_index(i)] = item
                return item
        return item
    
    
    def contains_item(self, new_item):
        # Check if the item already exists
        new_item = self.un_plural(new_item.lower())
        if not self.index_list:
            return False
        for item in self.index_list:
            if (item.lower() == new_item.lower()):
                return True
        return False
    
    def add_item(self, item):
        # pass item name, check plural, add to list
        item = self.un_plural(item.lower())
        if self.contains_item(item.lower()) == False:
            self.index_list.append(item.lower())
        
    def get_item(self,num):
        # pass index num to get name of item
        if num < self.size():
            return self.index_list[num]
        else:
            return 'none'
    
    def get_index(self, item):
        # pass item name and return index num
        item = self.un_plural(item.lower())
        return self.index_list.index(item.lower())
        
    def size(self):
        # return the size of index list
        return len(self.index_list)
        
    def __unicode__(self):
	    return self.index_list