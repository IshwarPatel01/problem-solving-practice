def find_it(seq):
    if not seq:
        return None
    
    result = seq[0]
    dict1 = {}
    dict2 = {}
    for i in seq:
        dict1[i] = dict1.get(i,0) + 1
    
    
    for key, value in dict1.items():
        if value % 2 == 1:
            dict2[key] = dict2.get(key,value)
    
    v= 0
    
    for key, value in dict2.items():
        if value > v:
            v = value
            result = key
    return result
            
​