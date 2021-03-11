from random import Random
class Key:
    def __init__(self,integer_val,integer_val2,string_val):
        self.integer_val = integer_val
        self.integer_val2 = integer_val2
        self.string_val = string_val
    
    def __hash__(self):
        return (self.integer_val * self.integer_val2) % len(self.string_val)


rand = Random()
lis_size = 16
lis = [0] * lis_size
for x in range(10000):
    key = Key(rand.randint(0,50),rand.randint(1,20),"thisissomefuckingbullshit")
    index = hash(key) % lis_size
    lis[index] += 1

print(lis)