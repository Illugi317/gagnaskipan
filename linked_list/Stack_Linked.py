class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __str__(self):
        string = ""
        node = self.top
        while node != None:
            string += str(node.data) + " "
            node = node.next
        return string

    def push(self, value):
        self.top = Node(value, self.top)
        self.size += 1

    def pop(self):
        if self.top == None:
            return self.top
        else:
            value = self.top.data
            self.top = self.top.next
            self.size -= 1
        return value
    
    def get_size(self):
        return self.size
    
if __name__ == '__main__':
    the_stack = Stack()
    the_stack.push(1)
    the_stack.push(2)
    the_stack.push(3)
    the_stack.push(4)
    the_stack.push(5)
    the_stack.push(6)
    the_stack.push(7)
    print(the_stack)
    print(the_stack.pop())
    print(the_stack)
