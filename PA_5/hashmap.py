from bucket import *

class HashMap(object):
    def __init__(self):
        self.size = 16
        self.buckets = [Bucket() for _ in range(self.size)]
        self.current_size = 0

    def insert(self,key,data):
        hashed_value = hash(key) % self.size
        self.buckets[hashed_value].insert(key,data)
        self.current_size += 1
        self.rebuild()

    def update(self, key, data):
        hashed_value = hash(key) % self.size
        self.buckets[hashed_value].update(key,data)
    
    def find(self,key):
        hashed_value = hash(key) % self.size
        return self.buckets[hashed_value].find(key)

    def contains(self,key):
        hashed_value = hash(key) % self.size
        return self.buckets[hashed_value].contains(key)

    def remove(self,key):
        hashed_value = hash(key) % self.size
        self.buckets[hashed_value].remove(key)
        self.current_size -= 1

    def rebuild(self):
        #when self.current_size is over 120% bigger than size rebuild. use this check in insert function
        if self.current_size > self.size * 1.2:
            new_list = [Bucket() for _ in range(self.size)]
            self.buckets += new_list
            self.size *= 2

    def __setitem__(self,key,data):
        hashed_value = hash(key) % self.size
        self.buckets[hashed_value][key] = data

    def __getitem__(self,key):
        return self.find(key)

    def __len__(self):
        return self.current_size

if __name__ == "__main__":
    a = HashMap()
    a.insert(2, "tveir")
    a.insert(3, "þrír")
    a.insert(4, "fjórir")
