class MyComparableKey:
    def __init__(self,int_val, string_val):
        self.int_val = int_val 
        self.string_val = string_val
    
    def __lt__(self,other):
        if self.int_val < other.int_val:
            return True
        elif self.int_val > other.int_val:
            return False
        elif self.int_val == other.int_val:
            #order of the strings ?
            if self.string_val < other.string_val:
                return True
            else:
                return False