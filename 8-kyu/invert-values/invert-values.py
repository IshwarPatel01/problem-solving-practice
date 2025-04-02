def invert(lst):
    arr =[]
    for i in range(len(lst)):
        if lst[i] < 0 :
            arr.append(abs(lst[i]))
        else:
            arr.append(-abs(lst[i]))
    return arr
    