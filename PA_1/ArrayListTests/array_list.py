class IndexOutOfBounds(Exception):
    pass

class Empty(Exception):
    pass

class ArrayList:
    def __init__(self):
        # TODO: remove 'pass' and implement functionality
        self.capacity = 4
        self.size = 0
        self.array = [0] * self.capacity

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        # TODO: remove 'pass' and implement functionality
        return_string = ""
        for x in range(self.size):
            return_string += str(self.array[x]) + ", "
        return return_string[:-2]

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        # TODO: remove 'pass' and implement functionality
        if self.size == self.capacity:
            self.array = self.resize()
        for x in range(self.size,-1,-1):
            self.array[x] = self.array[x-1]
        self.array[0] = value
        self.size += 1

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        # TODO: remove 'pass' and implement functionality
        if index > self.size or index < 0:
            raise IndexOutOfBounds()
        elif self.size == self.capacity:
            self.array = self.resize()
        for x in range(self.size,index,-1):
            self.array[x] = self.array[x-1]
        self.array[index] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def append(self, value):
        # TODO: remove 'pass' and implement functionality
        if self.size == self.capacity:
            self.array = self.resize()
        self.array[self.size] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # TODO: remove 'pass' and implement functionality
        if index >= self.size or index < 0:
            raise IndexOutOfBounds()
        self.array[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        # TODO: remove 'pass' and implement functionality
        if self.size == 0:
            raise Empty()
        return self.array[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        # TODO: remove 'pass' and implement functionality
        if index >= self.size or index < 0:
            raise IndexOutOfBounds()
        return self.array[index]

    #Time complexity: O(1) - constant time
    def get_last(self):
        # TODO: remove 'pass' and implement functionality
        if self.size == 0:
            raise Empty()
        return self.array[self.size - 1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        # TODO: remove 'pass' and implement functionality
        self.capacity *= 2
        new_array = [0] * self.capacity
        for x in range(self.size):
            new_array[x] = self.array[x]
        return new_array

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        # TODO: remove 'pass' and implement functionality
        if index >= self.size or index < 0:
            raise IndexOutOfBounds()
        for x in range(index, self.size - 1):
            self.array[x] = self.array[x+1]
        self.array[self.size - 1] = 0
        self.size -= 1
        
    #Time complexity: O(1) - constant time
    def clear(self):
        # TODO: remove 'pass' and implement functionality
        self.array = [0] * self.capacity
        self.size = 0

    #Time complexity: O(n) - linear time in size of sublist
    def sublist(self, start, length):
        # TODO: remove 'pass' and implement functionality
        if start < 0 or length <= 0 or start+length > self.size:
            raise IndexOutOfBounds()
        new_arr = ArrayList()
        for x in range(start, start+length, 1):
            new_arr.append(self.array[x])
        return new_arr

    #Time complexity: O(n) - linear time in size of concatinated list
    # OR
    #Time complexity: O(n+m) - linear time in size of both lists, self and other
    def concatenate(self, other):
        # TODO: remove 'pass' and implement functionality
        concated = ArrayList()
        for x in range(self.size):
            concated.append(self.array[x])
        for i in range(other.size):
            concated.append(other.array[i])
        return concated
      

if __name__ == "__main__":
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level
    pass