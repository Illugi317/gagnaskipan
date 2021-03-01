def less_than(a, b,counter=0):  # ONLY NEEDS TO WORK FOR POSITIVE INTEGERS
    #TODO: remove 'pass' and implement functionality
    #is A less than B?
    if a == b:
        return False
    elif a+counter == b:
        return True
    elif a == b+counter:
        return False
    else:
        return less_than(a,b,counter+1)

def linear_search(lis,value):
    if lis == []:
        return False
    elif lis[-1] == value:
        return True
    return linear_search(lis[1:],value)

def unique(lis1):
    if lis1 == []:
        return []
    if linear_search(lis1[:-1],lis1[-1]):
        return unique(lis1[:-1])
    return unique(lis1[:-1]) + [lis1[-1]]

# FEEL FREE TO EDIT THE TESTS AND MAKE THEM BETTER
# REMEMBER EDGE CASES!

def test_less_than(num1, num2):
    if(less_than(num1, num2)):
        print(str(num1) + " is less than " + str(num2))
    else:
        print(str(num1) + " is NOT less than " + str(num2))

def test_unique(lis1):
    print(str(unique(lis1)) + " are the unique items in " + str(lis1))

def run_recursion_program():

    print("\nTESTING LESS THAN:\n")

    test_less_than(8, 3)
    test_less_than(2, 9)
    test_less_than(4, 17)
    test_less_than(11, 3)
    test_less_than(8, 2)
    test_less_than(8, 7)
    test_less_than(7, 8)
    test_less_than(6, 16)
    test_less_than(7, 7)

    print("\nTESTING UNIQUE:\n")

    test_unique(['a', 'f', 'd', 't', 'a', 'b', 'c', 'd', 'e'])
    test_unique(['a', 'b', 'f', 'g', 'a', 't', 'c', 'a', 'b', 'c', 'd', 'e'])
    test_unique(['f', 'g', 't', 'a', 'b', 'c', 'd', 'e'])
    test_unique(['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'])
    test_unique(['t'])


if __name__ == "__main__":
    run_recursion_program()