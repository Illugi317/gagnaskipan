class Node(object):
    def __init__(self, key=None, value=None, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node
    
    def __hash__(self):
        if type(self.key) == int:
            return self.key

        if type(self.key) == str:
            ret_val = 0
            for char in self.key:
                ret_val <<= 7
                ret_val += ord(char)
        
        if type(self.key) == float:
            return int(self.key * 9952)

class LinkedList(object):
    def __init__(self):
        self.head = Node()
        self.size = 0

    def add(self,key,value):
        new_node = Node(key,value,self.head.next)
        self.head.next = new_node
        self.size += 1

    def __iter__(self):
        current = self.head.next
        while current != None:
            yield current
            current = current.next

    def remove(self, key):
        lag = self.head
        for node in iter(self):
            if node.key == key:
                lag.next = lag.next.next
                self.size -=1
            lag = node



if __name__ == '__main__':
    l = LinkedList()
    l.add(1,"rassgat")
    l.add(2,"johann")
    l.add(3,"ég drep þig")
    for node in iter(l):
        print(f"{node.key}:{node.value}")
    l.remove(2)
    for node in iter(l):
        print(f"{node.key}:{node.value}")  



