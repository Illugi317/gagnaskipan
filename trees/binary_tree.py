class BT_Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def populate_tree(self):
        self.root =  self.populate_tree_recur("root",0,"")

    def populate_tree_recur(self, parent_name, level, left_right_string):
        data = ""
        if left_right_string == "":
            data = input("enter the name of the root :")
        else:
            data = input(("*" * level)+"enter the data of the "+left_right_string+ " node with parent node "+parent_name +": ")
        if data == "":
            return None
        node = BT_Node(data)
        node.left = self.populate_tree_recur(data,level+1,"left")
        node.right = self.populate_tree_recur(data,level+1,"right")
        return node

    def print_preorder(self):
        self.print_preorder_recur(self.root)
    
    def print_preorder_recur(self, node):
        if node == None:
            return
        #pre
        print(node.data)
        self.print_preorder_recur(node.left)
        #in
        self.print_preorder_recur(node.right)
        #post

    def print_inorder(self):
        self.print_inorder_recur(self.root)
    
    def print_inorder_recur(self, node):
        if node == None:
            return
        #pre
        self.print_inorder_recur(node.left)
        #in
        print(node.data)
        self.print_inorder_recur(node.right)
        #post

    def print_postorder(self):
        self.print_postorder_recur(self.root)
    
    def print_postorder_recur(self, node):
        if node == None:
            return
        #pre
        self.print_postorder_recur(node.left)
        #in
        self.print_postorder_recur(node.right)
        #post
        print(node.data)


# tree = BinaryTree()
# tree.populate_tree()
# tree.print_preorder()

class GEN_Node:
    def __init__(self, data=None):
        self.data = data
        self.children = []

class General_tree:
    def __init__(self):
        self.root = None

    def populate_tree(self):
        self.root = self.populate_tree_recur("root",0,0,True)


    def populate_tree_recur(self, parent_name, level, child_counter,is_root):
        data = ""
        if is_root:
            data = input("Enter name of root node :")
        else:
            data = input(("*"*level)+"Enter data of node with parent_node "+parent_name)
        if data == "":
            return None
        node = GEN_Node(data)
        add_more_children = "y"
        while add_more_children != "n":
            if add_more_children == "y":
                node.children.append(self.populate_tree_recur(data,level,child_counter+1,False))
            add_more_children = input(f"Would you like to add more children? (Current count: {child_counter+1} y:yes n:no) Parent will be : {data} :")
        return node

    '''
    def populate_tree_recur(self, parent_name, level, r_string, child_counter):
        data = ""
        if r_string == "":
            data = input("enter the name of the root :")
        else:
            data = input(("*" * level)+"enter the data of the "+r_string+ " node with parent node "+parent_name +": ")
        if data == "":
            return None


        node = GEN_Node(data)
        if child_counter < 11:
            node.children.append(self.populate_tree_recur(data,level,"next",child_counter+1))
        else:
            node.children.append(self.populate_tree_recur(data, level+1, "next",0))
        return node
    '''

a = GEN_Node("yes")
a.children.append(GEN_Node("no"))
print(a.data)
print(a.children)
print(a.children[0].data)

tree = General_tree()
tree.populate_tree()
print(tree)
    