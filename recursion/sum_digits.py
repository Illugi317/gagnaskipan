def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return int(n % 10) + sum_of_digits(int(n/10))
