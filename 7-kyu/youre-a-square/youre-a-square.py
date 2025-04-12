def is_square(n):    
    if n < 0:
        return False  # Negative numbers are not perfect squares
    i = 0
    
    while i * i <= n:
        if i * i == n:
            return True
        i += 1
    return False
        