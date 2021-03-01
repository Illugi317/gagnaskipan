class Node:
    def __init__(self, data = None, next_val = None):
        self.data = data
        self.next_val = next_val


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push_back(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next_val = new_node

        self.tail = new_node
        self.size += 1

    def push_front(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.size += 1
        else:
            new_node.next_val = self.head
            self.head = new_node
            self.size += 1
        
    def pop_front(self):
        if self.size == 0:
            return None
        else:
            front_element = self.head.data
            self.head = self.head.next_val
            self.size -= 1
            return front_element

    def pop_back(self):
        if self.size == 0:
            return None
        else:
            value = self.tail.data
            node = self.head
            while node.next_val != self.tail:
                if self.size == 1:
                    break
                node = node.next_val
            self.tail = node
            self.tail.next_val = None
        self.size -=1
        return value

    def get_size(self):
        return self.size

    def __str__(self):
        if self.size == 0:
            return ""
        string = ""
      
        node = self.head
        while node != None:
            string += str(node.data) + " "
            node = node.next_val

        return string
    
