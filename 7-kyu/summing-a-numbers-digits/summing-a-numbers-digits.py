def sum_digits(n):
    result = 0
    n = abs(n)    
    while n != 0:
        last = n % 10
        result += last
        n //= 10
    return result
        