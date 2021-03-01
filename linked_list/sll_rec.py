class Node:
    def __init__(self, data = None, next_val = None):
        self.data = data
        self.next = next_val

def linear_search(head, value):
    if head == None:
        return False
    if value == head.data:
        return True
    else:
        return linear_search(head.next,value)

def delete_every_other(head):
    return deo_helper(head,0)

def deo_helper(head, i):
    if head == None:
        return None
    if i % 2 == 1:
        head.next = deo_helper(head.next,i+1)
        return head
    else:
        return deo_helper(head.next, i+1)

### start of nr.10
head = Node(1,Node(2,Node(3,Node(4,Node(5)))))

def length_of_sll_rec(head):
    if head == None:
        return 0
    else:
        return 1 + length_of_sll_rec(head.next)

print(length_of_sll_rec(head))

def length_of_sll_it(head):
    counter = 0
    while head != None:
        counter += 1
        head = head.next
    return counter

print(length_of_sll_it(head))


def sum_of_sll_it(head):
    counter = 0
    while head != None:
        counter += head.data
        head = head.next
    return counter

print(sum_of_sll_it(head))

def sum_of_sll_rec(head):
    if head == None:
        return 0
    else:
        return head.data + sum_of_sll_rec(head.next)

print(sum_of_sll_rec(head))

def insert_ordered(head, value):
    while head != None:
        if head.data == value:
            new_node = Node(value,head.next)
        head = head.next


