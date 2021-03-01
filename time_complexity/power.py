def multi(a,b):
    if a > b:
        temp = a
        a = b
        b = temp
    result = 0
    for i in range(a):
        result += b
    return result


