 
def get_real_floor(n):
​
    if n == 1:
        return 0
    elif n < 13:
        return n - 1
    elif n > 13:
        return n - 2