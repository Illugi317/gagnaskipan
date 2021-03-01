class Queue:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.array = [0] * self.capacity
        self.head = 0
        self.tail = 0

    #implement O(1) with start index and stop index2
    def remove(self):
        if self.size == 0:
            return None
        tmp = self.array[self.head]
        self.head += 1
        self.size -= 1
        return tmp

    def add(self, value):
        if self.tail == self.capacity:
            self.array = self.resize()
        self.array[self.tail] = value
        self.size += 1
        self.tail += 1

    def get_size(self):
        if self.tail == 0 and self.head == 0:
            return 0
        else: 
            return self.tail - self.head

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
    print("size:",a.get_size())
    a.add(4)
    print(a.remove())
    a.add(5)
    a.add(6)
    print(a.remove())
    a.add(7)
    a.add(8)
    print("size:",a.get_size())
    print(a.remove())
    print("size:",a.get_size())