def delete_nth(order,n):
    count = {}
    arr = []
    
    for item in order:
        if count.get(item,0) < n:
            arr.append(item)
            count[item] = count.get(item,0) + 1
    return arr
            
    
    