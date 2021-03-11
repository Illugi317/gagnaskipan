class BST_Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left #vinstri
        self.right = right #hægri
    
    def __str__(self):
        if self.left != None and self.right != None:
            return f"{str(self.left)} {str(self.data)} {str(self.right)}"

        elif self.left != None and self.right == None:
            return f"{str(self.left)} {str(self.data)}"
        
        elif self.left == None and self.right != None:
            return f"{str(self.data)} {str(self.right)}"

        elif self.left == None and self.right == None:
            return f"{str(self.data)}"

class ADT:
    def __init__(self):
        self.root = None
        self.__size = 0

    def add(self,value):
        self.root = self.__add_recursive(value,self.root)
        self.__size += 1

    def __add_recursive(self,value,current_node):
        if current_node == None:
            return BST_Node(value)
        elif current_node.data > value:
            current_node.left = self.__add_recursive(value,current_node.left)
        elif current_node.data < value:
            current_node.right = self.__add_recursive(value,current_node.right)
        return current_node

    def contains(self, value):
        return self.__find(value,self.root)

    def __find(self,value, current_node):
        if current_node.data == value:
            return True
        elif current_node.left == None and current_node.right == None:
            return False
        elif current_node.data > value:
            return self.__find(value,current_node.left)
        elif current_node.data < value:
            return self.__find(value,current_node.right)

    def remove(self, value):
        pass

    def remove_recursive(self,current_node,value):
        node_to_delete = self.__find_node_of_value(value,current_node)
        # Leaf
        if node_to_delete.left == None and node_to_delete.right == None:
            parent_node = self.__find_parent_node(value,self.root)
            if parent_node.left.data == value:
                parent_node.left = None
            elif parent_node.right.data == value:
                parent_node.right = None
            return
        # Move child to another parent
        elif node_to_delete.left is not None and node_to_delete.right is not None:
            pass

    def __find_parent_node(self,value,current_node):
        if current_node.left.data == value or current_node.right.data == value:
            return current_node
        elif current_node.data > value:
            return self.__find_parent_node(value,current_node.left)
        elif current_node.data < value:
            return self.__find_parent_node(value,current_node.right)

    def __find_node_of_value(self, value,current_node):
        if current_node.data == value:
            return current_node
        elif current_node.left == None and current_node.right == None:
            return False
        elif current_node.data > value:
            return self.__find_node_of_value(value,current_node.left)
        elif current_node.data < value:
            return self.__find_node_of_value(value,current_node.right)

    def __find_rightmost(self,current_node):
        if current_node.right == None:
            return current_node
        return self.__find_rightmost(current_node.right)

    def __len__(self):
        return self.__size

    def __str__(self):
        return str(self.root)