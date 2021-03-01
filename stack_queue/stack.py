class Stack:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.array = [0] * self.capacity

    def __str__(self):
        ret_str = ""
        for x in range(self.size):
            ret_str += f"{self.array[x]}, "
        return ret_str[:2]
    
    def push(self, value):
        if self.size == self.capacity:
            self.array = self.resize()
        self.array[self.size] = value
        self.size += 1 

    def pop(self):
        self.size -= 1
        return self.array[self.size]

    def resize(self):
        self.capacity *= 2
        new_array = [0] * self.capacity
        for x in range(self.size):
            new_array[x] = self.array[x]
        return new_array

if __name__ == '__main__':
    a = Stack()
    a.push(1)
    a.push(2)
    a.push(3)
    a.push(4)
    a.push(5)
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())

