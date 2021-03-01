def recursion_multi(a,b):
    if a == 0:
        return 0
    elif a == 1:
        return b
    else:
        return b + recursion_multi(a-1,b)
