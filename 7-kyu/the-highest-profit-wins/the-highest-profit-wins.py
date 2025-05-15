 
def min_max(lst):
    min = lst[0]
    max = lst[0]
    
    for i in range(1,len(lst)):
        if lst[i] < min:
            min = lst[i]
        elif lst[i] > max:
            max = lst[i]
    return [min,max]