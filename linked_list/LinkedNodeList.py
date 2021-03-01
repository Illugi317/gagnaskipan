class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

class LinkedNode:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __str__(self):
        string = ""
        node = self.head
        while node != None:
            string += str(node.data) + " "
            node = node.next
        return string

    def push_front(self, value):
        self.head = Node(value,  self.head)
        if self.tail == None:
            self.tail = self.head
        self.size += 1

    def push_back(self, value):
        if self.head == None:
            self.head = Node(value, None)
            self.tail = Node(value, None)
        else:
            self.tail.next = Node(value,None)
            self.tail = self.tail.next
        self.size += 1

    def pop_front(self):
        if self.tail == None:
            return self.tail
        value = self.head.data
        self.head = self.head.next
        
        if self.head == None:
            self.tail = self.head
        return value

    def pop_back(self):
        if self.head == None:
            return self.head
        else:
            value = self.tail.data
            node = self.head
            while node.next != None:
                node = node.next
            self.tail = node
            self.tail.next = None
        self.size -= 1
        return value

    def get_size(self):
        return self.size

if __name__ == '__main__':
    linked = LinkedNode()
    linked.push_front(1)
    linked.push_front(2)
    linked.push_front(3)
    linked.push_front(4)
    linked.push_back(5)
    print(linked)
    first = linked.pop_back()
    last = linked.pop_front()
    print(f"First: {first}, Last: {last}, All list: {str(linked)}")