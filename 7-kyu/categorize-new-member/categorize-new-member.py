def open_or_senior(data):
    arr = []
    n = len(data)
    for i in range(n):
        if data[i][0] >= 55 and data[i][1] > 7:
            arr.append("Senior")
        else:
            arr.append("Open")
    return arr
       
               
    