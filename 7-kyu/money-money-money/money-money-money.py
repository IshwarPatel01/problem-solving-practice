 
def calculate_years(p, i, t, d):
    if p >= d:
        return 0
    years = 0
    
    while p < d:
        p += p * i * (1 -t)
        years += 1
    return years
    
    
    
    
​