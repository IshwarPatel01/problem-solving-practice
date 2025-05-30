def stray(arr):
    count = {}
    
    for num in arr:
        count[num] = count.get(num, 0) + 1
    
    for num , count in count.items():
        if count == 1:
            return num
    return None