def add_length(str_):
    arr = []
    arr2 = str_.split()
    result = ""
    for item in arr2:
        result =  item + " " + str(len(item) )
        arr.append( result)
    return arr
    #your code here