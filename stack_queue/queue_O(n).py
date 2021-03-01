class Queue:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.array = [0] * self.capacity

    def remove(self): #first implementation O(n)
        a = self.array[0]
        self.shift_list_left()
        self.size -= 1
        return a

    def shift_list_left(self):
        for x in range(self.size):
            if x+1 >= self.capacity:
                continue
            self.array[x] = self.array[x+1]
    
    def add(self, value):
        if self.size == self.capacity:
            self.array = self.resize()
        self.array[self.size] = value
        self.size += 1

    def resize(self):
        self.capacity *= 2
        new_array = [0] * self.capacity
        for x in range(self.size):
            new_array[x] = self.array[x]
        return new_array

if __name__ == '__main__':
    a = Queue()
    a.add(1)
    a.add(2)
    a.add(3)
    a.add(4)
    a.add(5)
    a.add(6)
    a.add(7)
    a.add(8)
    print(a.remove())