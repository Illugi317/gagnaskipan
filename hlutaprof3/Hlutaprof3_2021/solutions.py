class HashTable:
    def __init__(self):
        #set a fixed  capacity
        self.capacity = 16
        #create the bucketlist
        self.bucket_list = []

        #fill the bucketlist with empty arrays
        for i in range(self.capacity):
            self.bucket_list.append([])
    
    def insert(self, key):
        if not self.contains(key):
            idx = hash(key) % self.capacity
            sub_list = self.bucket_list[idx]
            sub_list.append(key)

    def contains(self, key):
        idx = hash(key) % self.capacity
        sub_list = self.bucket_list[idx]
        if key in sub_list:
            return True
        else:
            return False

    def remove(self, key):
        if self.contains(key):
            idx = hash(key) % self.capacity
            sub_list = self.bucket_list[idx]
            sub_list.remove(key)


class PrefixParsingTreeNode:
    def __init__(self, token, left, right):
        self.token = token
        self.left = left
        self.right = right

class PrefixParsingTree:
    def __init__(self):
        self.root = None

    class Tokenizer:
        def __init__(self, str_statement):
            self.statement = str_statement
            self.position = 0

        def get_next_token(self):
            i = self.position
            while i < len(self.statement) and self.statement[i] != " ":
                i += 1
            ret_val = self.statement[self.position:i]
            self.position = i + 1
            return ret_val

    def build_tree_recursive(self, tokenizer):
        token = tokenizer.get_next_token()

        if token == "+" or token == "-":
            return PrefixParsingTreeNode(token, self.build_tree_recursive(tokenizer), self.build_tree_recursive(tokenizer))
        elif token.isdigit():
            return PrefixParsingTreeNode(token, None, None)
        else:
            return PrefixParsingTreeNode(token, None, None)

    def load_statement_string(self, statement):
        tokenizer = self.Tokenizer(statement)
        self.root = self.build_tree_recursive(tokenizer)

    def calculate_value(self):
        # IMPLEMENT THIS OPERATION
        # YOU CAN MAKE HELPER FUNCTIONS IN THE CLASS AS NEEDED
        node = self.root
        return self.calculate_value_rec(node)
    
    def calculate_value_rec(self, node):
        if node.right is None and node.left is None:
            return node.token
        left_val, right_val = self.calculate_value_rec(node.left),self.calculate_value_rec(node.right)
        if not node.token.isdigit():
            return self.evaluate(node.token,left_val,right_val)

    def evaluate(self,operator,num_1, num_2):
        if operator == '+':
            return int(num_1) + int(num_2)
        elif operator == '-':
            return int(num_1) - int(num_2)

class GeneralNode:
    def __init__(self,value):
        self.value = value
        self.children = []
    
    def add_child(self,obj):
        self.children.append(obj)

class General_Tree:
    def __init__(self):
        self.root = None

    class Tokenizer_GEN:
        def __init__(self, str_statement):
            self.statement = str_statement
            self.position = 2

        def get_next_token(self):
            i = self.position
            while i < len(self.statement) and self.statement[i] != "{":
                i += 1
            ret_val = self.statement[self.position:i]
            self.position = i + 1
            return ret_val

    def build_tree_recursive(self, tokenizer):
        token = tokenizer.get_next_token()
        if token == "":
            return
        node = GeneralNode(token)
        while True:
            child_node = self.build_tree_recursive(tokenizer)
            if child_node is None:
                break
            if "}}" in child_node.value:
                child_node.value = child_node.value[0:len(child_node.value)-2]
            if "}" in child_node.value:
                child_node.value = child_node.value[0:len(child_node.value)-1]
            node.children.append(child_node)
        return node
                
    def load_statement_string(self, statement):
        tokenizer = self.Tokenizer_GEN(statement)
        self.root = self.build_tree_recursive(tokenizer)

'''
            self.root
           /          \ 
        kennarar    nemendur
'''


def parse_bracket_file(filename):
    # IMPLEMENT THIS OPERATION
    # YOU CAN IMPLEMENT ONE OR MORE CLASSES
    # YOU CAN MAKE HELPER FUNCTIONS AS NEEDED
    input_file = open(filename)
    string = input_file.read()
    gen = General_Tree()
    gen.load_statement_string(string)
    return gen

def write_bulleted_file(filename, my_tree):
    # IMPLEMENT THIS OPERATION
    # YOU CAN IMPLEMENT ONE OR MORE CLASSES
    # YOU CAN MAKE HELPER FUNCTIONS AS NEEDED
    output_file = open(filename, "w")

def write_labelled_file(filename, my_tree):
    # IMPLEMENT THIS OPERATION
    # YOU CAN IMPLEMENT ONE OR MORE CLASSES
    # YOU CAN MAKE HELPER FUNCTIONS AS NEEDED
    output_file = open(filename, "w")

def test_hash_table():
    t = HashTable()
    t.insert("test1")
    t.insert("test2")
    t.insert("test3")
    t.insert("test1")
    print(t.contains("test3"))
    print(t.contains("test1"))
    print(t.contains("test4"))
    t.remove("test3")
    print(t.contains("test3"))
    t.remove("test1")
    print(t.contains("test2"))
    print(t.contains("test1"))

# OPERATION FOR TESTING THE PREFIX PARSING TREE
# DONT CHANGE
def test_prefix_tree(statement_string):
    print("This is the statement: " + statement_string)
    ppt = PrefixParsingTree()
    ppt.load_statement_string(statement_string)
    print("This is the result: " + str(ppt.calculate_value()))

# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!
    print("testing hash table")
    test_hash_table()

    print("testing prefix tree")
    test_prefix_tree("- 12 + 4 5")
    test_prefix_tree("+ 12 + - 21 5 5")
    test_prefix_tree("+ 4 + - 4 6 - 9 8")
    test_prefix_tree("- + - + 6 9 8 + 1 + 5 5 - - + 6 7 - 9 8 - + 9 6 1")
    test_prefix_tree("+ + 8 4 - + - 3 3 2 - + 7 8 9")


    bullet_list_tree = parse_bracket_file("bracket_file_01.txt")
    #write_bulleted_file("bullet_file_01.txt", bullet_list_tree)
    #write_labelled_file("label_file_01.txt", bullet_list_tree)