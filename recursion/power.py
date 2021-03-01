def power(base,exp):
    if exp==1:
        return base
    if exp!=1:
        return base*power(base,exp-1)

if __name__ == '__main__':
    print(power(-2,5))