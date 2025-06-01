 
def no_boring_zeros(n):
    s = str(n)
​
    while s.endswith('0') and s != '0':
        s = s[:-1]
    return int(s)
        
        
         