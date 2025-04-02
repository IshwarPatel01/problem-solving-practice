def get_middle(s):
    n = len(s)
    i = n // 2
    if n % 2 == 0:
        return s[i-1] + s[i]
    return s[i]
        
        
    