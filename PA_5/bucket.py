from linked_list import *

class NotFoundException(Exception): pass
class ItemExistsException(Exception): pass

class Bucket(object):
    def __init__(self):
        self.ll = LinkedList()

    def insert(self,key,data):
        if not self.contains(key):
            self.ll.add(key,data)
        else:
            raise ItemExistsException

    def update(self,key,data):
        if self.contains(key):
            node_to_update = self._return_node(key)
            node_to_update.value = data
        else:
            raise NotFoundException

    def _return_node(self,key):
        for x in self.ll:
            if x.key == key:
                return x
        raise NotFoundException

    def find(self,key):
        for x in self.ll:
            if x.key == key:
                return x.value
        raise NotFoundException

    def contains(self,key):
        for x in self.ll:
            if x.key == key:
                return True
        return False

    def remove(self,key):
        if self.contains(key):
            self.ll.remove(key)
        else:
            raise NotFoundException
    
    def __setitem__(self,key,data):
        if self.contains(key):
            self.update(key,data)
        else:
            self.insert(key,data)

    def __getitem__(self,key):
        return self.find(key)

    def __len__(self):
        return self.ll.size

if __name__ == '__main__':
    b = Bucket()
    b.insert(10,"nei")
    b.insert(40,"sammála")
    b.insert(20,"fokk off")
    try:
        b.insert(20,"ops")
    except:
        print("WORKS")
    print(len(b))
    print(b[10])
    b[100] = "Illugi"
    print(b[100])
