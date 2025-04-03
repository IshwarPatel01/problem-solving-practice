def digitize(n):
    n = str(n)
    arr = []
    for i in range(len(n) - 1 ,- 1, - 1):
        arr.append(int(n[i]))
        
    return arr
    
    
    