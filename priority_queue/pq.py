class HeapNode:
    def __init__(self,priority, data=None,parent = None ,left = None, right = None):
        self.priority = priority
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right


class PriorityQueue:
    def __init__(self):
        self.root = None
        self.last_node = None

    def swap(self, node_1, node_2):
        n1_pri = node_1.priority
        n1_data = node_1.data
        node_1.priority = node_2.priority
        node_1.data = node_2.data
        node_2.priority = n1_pri
        node_2.data = n1_data
    
    def add(self, priority, data):
        if self.root is None:
            self.last_node = self.root = HeapNode(priority, data)
        elif self.last_node.parent != None and self.last_node is self.last_node.parent.left:
            self.last_node.parent.right = HeapNode(priority, data, self.last_node.parent)
            self.last_node = self.last_node.parent.right
        else:
            next_add = self.last_node
            while next_add is not self.root and next_add is next_add.parent.right:
                next_add = next_add.parent
            if next_add is not self.root:
                next_add = next_add.parent.right
            
            while next_add != None:
                next_add = next_add.left
            
            next_add.left = HeapNode(priority, data,next_add)
            self.last_node = next_add.left
        node = self.last_node
        while node.parent != None and node.priority < node.parent.priority:
            self.swap(node,node.parent)
            node = node.parent
        
    def remove(self):
        if self.last_node == None:
            return None
        ret_val = self.root.data
        if self.last_node is self.root:
            self.last_node = self.root = None
            return ret_val
        self.swap(self.last_node, self.root)
        if self.last_node is self.last_node.parent.right:
            self.last_node = self.last_node.parent.left
            self.last_node.parent.right = None
        else:
            self.last_node = self.last_node.parent
            self.last_node.left = None
            while self.last_node is not self.root and self.last_node is self.last_node.parent.left:
                self.last_node = self.last_node.parent

            if self.last_node is not self.root:
                self.last_node = self.last_node.parent.left

            while self.last_node.right != None:
                self.last_node = self.last_node.right
        
        node = self.root

        while node.left != None:
            if node.right != None and node.right.priority < node.priority:
                if node.left.priority < node.right.priority:
                    self.swap(node,node.left)
                    node = node.left
                else:
                    self.swap(node, node.right)
                    node = node.right
            elif node.left.priority < node.priority:
                self.swap(node,node.left)
                node = node.left
            else:
                break
        return ret_val

    def is_empty(self):
        return self.root == None