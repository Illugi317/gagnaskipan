
def is_divisible(a, b):
    if a==b or a == 0:
        return True
    elif a < b or b == 0:
        return False
    else:
        return is_divisible(a-b,b)

print(is_divisible(0,0))