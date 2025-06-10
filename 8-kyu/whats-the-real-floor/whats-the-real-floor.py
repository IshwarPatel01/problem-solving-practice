 
def get_real_floor(n):
    # code here
    if n == 0 or n == 1:
        return 0
    
    if n < 13:
        return n - 1
    elif n > 13:
        return n - 2