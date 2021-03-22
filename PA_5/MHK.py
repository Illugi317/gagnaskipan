class MyHashableKey:
    def __init__(self,int_value, string_value):
        self.int_value = int_value
        self.string_value = string_value

    def __eq__(self,other):
        if self.int_value == other.int_value and self.string_value == other.string_value:
            return True
        else:
            return False

    def __hash__(self):
        if self.int_value < 0:
            return -1 * self.int_value
        else:
            return self.int_value