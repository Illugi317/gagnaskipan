class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class BSTMap_Node:
    def __init__(self,data=None,key=None,left=None,right=None):
        self.data = data
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BSTMap:
    def __init__(self):
        self.root = None
        self.__size = 0

    def insert(self,key ,data):
        self.root = self.__insert_recursive(data, key, self.root)
        self.__size += 1
    
    def __insert_recursive(self,data,key,node):
        #a[key] = data
        if node is None:
            return BSTMap_Node(data,key)
        elif node.key == key:
            raise ItemExistsException()
        elif node.key > key:
            node.left = self.__insert_recursive(data,key,node.left)
        elif node.key < key:
            node.right = self.__insert_recursive(data,key,node.right)
        return node

    def update(self,key, data):
        node_to_check = self.__find_node(key,self.root)
        if node_to_check is None:
            raise NotFoundException()
        node_to_check.data = data

    def __find_node(self, key, node):
        if node is None:
            raise NotFoundException()
        elif node.key == key:
            return node
        elif node.left == None and node.right == None or node is None:
            raise NotFoundException()
        elif node.key > key:
            return self.__find_node(key,node.left)
        elif node.key < key:
            return self.__find_node(key,node.right)

    def find(self, key):
        node = self.__find_node(key,self.root)
        return f"{node.key}:{node.data}"

    def contains(self,key):
        try:
            self.find(key)
        except:
            return False
        return True

#    def remove(self,key):
#        pass #fuck this function and their mothers

    def remove(self, key):
        self.root = self.__remove(key, self.root)
        self.__size -= 1

    def __remove(self, key, node):
        if node is None:
            return None
        if not self.contains(key):
            raise NotFoundException()
        if node.key == key:
            if node.left is None and node.right is None:
                return None

            elif node.left is None and node.right is not None:
                return node.right

            elif node.left is not None and node.right is None:
                return node.left

            else:
                successor = self.__find_inorder_successor(node.key, node.right)
                node.key = successor.key
                node.right = self.__remove(successor.key, node.right)
                return node

        if key < node.key:
            node.left = self.__remove(key, node.left)
        if key > node.key:
            node.right = self.__remove(key, node.right)

        return node

    def __find_inorder_successor(self, key, node, current_lowest=None):
        if current_lowest is None or node.key < current_lowest.key:
            current_lowest = node
            return current_lowest

        if node.left is not None:
            current_lowest = self.__find_inorder_successor(key, node.left, current_lowest)

        if node.right is not None:
            current_lowest = self.__find_inorder_successor(key, node.right, current_lowest)

        return current_lowest

    def __setitem__(self, key, data):
        try:
            self.update(key,data)
        except:
            self.insert(key, data)

    def __getitem__(self, key):
        node = self.__find_node(key,self.root)
        return str(node.data)
    
    def __len__(self):
        return self.__size
    
    def __str__(self):
        string_list = []
        self.tree_to_string(self.root, string_list)
        return ''.join(sorted(string_list))

    def tree_to_string(self,node,string):
        if node is None:
            return
        string.append(f"{{{node.key}:{node.data}}} ")
        if node.left is None and node.right is None:
            return
        self.tree_to_string(node.left, string)
        if node.right is not None:
            self.tree_to_string(node.right, string)
            
        
        

if __name__ == '__main__':
    a = BSTMap()
    a.insert(6,'Maria')
    a.insert(3,'Jóhann')
    a.insert(2,'Angus')
    a.insert(9,'Haraldur')
    a.insert(7,'Jósefína')
    a.insert(8,'Gullbrá')
    print(a)
