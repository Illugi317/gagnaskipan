'''
class Dequeue:
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

    def push_front(self,value):
        pass

    def push_back(self,value):
        pass 

    def pop_front(self,value):
        pass
    
    def pop_back(self,value):
        pass



    def get_size(self):
        if self.tail == 0 and self.head == 0:
            return 0
        elif self.tail == self.head: 
            return None
        else:
            return self.tail - self.head

    def resize(self):
        self.capacity *= 2
        new_array = [0] * self.capacity
        for x in range(self.size):
            new_array[x] = self.array[x]
        return new_array
'''

#kill me now
class Deque():
    def __init__(self):
        self.size = 1
        self.deque = [None]*self.size
        self._n = 0
        self._front = 0
 
    def __str__(self):
        return str(self.deque)
 
    def __resize(self):
        if self._n == self.size:
            old = self.deque
            self.deque = [None] * 2
            walk = self._front
            for i in range(self.size):
                self.deque[i] = old[walk]
                walk = (1 + walk) % len(old)
            self._front = 0
 
    def push_front(self, value):
        self.__resize()
        
        self.deque[self._front] = value
        self._front += 1
 
    def push_back(self, value):
        self.__resize()
        self.deque[self._n] = value
        self._n += 1
 
    def pop_front(self):
        answer = self.deque[0]
        self.deque[self._front] = None
        self._front = (self._front + 1) % len(self.deque)
        self._n -= 1
        return answer
 
    def pop_back(self):
        answer = self.deque[self._n-1]
        self.deque[self._n - 1] = None
        self._n -= 1
        return answer
 
 
if __name__ == "__main__":
    deque = Deque()
    deque.push_back(4)
    deque.push_back(5)
    deque.pop_front()
    print(deque)