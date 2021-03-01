class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

class QueueNode:
    def __init__(self,head = None, tail = None, size = 0):
        self.head = head
        self.tail = tail
        self.size = size
    
    def __str__(self):
        node = self.head
        string = ""
        while node != None:
            string += str(node.data) + " "
            node = node.next
        return string
    
    def add(self,value):
        if self.head == None:
            self.head = self.tail = Node(value, None)
        else:
            self.tail.next = Node(value, None)
            self.tail = self.tail.next
        self.size += 1
    
    def remove(self):
        if self.head == None:
            return self.head

        value = self.head.data
        self.head = self.head.next
        
        if self.head == self.tail:
            self.tail = self.head
        return value

if __name__ == '__main__':
    q = QueueNode()
    q.add(1)
    q.add(2)
    q.add(3)
    q.add(4)
    q.add(5)
    q.add(6)
    print(q)
    print(q.remove())
    print(q)
    print(q.remove())
    print(q)

