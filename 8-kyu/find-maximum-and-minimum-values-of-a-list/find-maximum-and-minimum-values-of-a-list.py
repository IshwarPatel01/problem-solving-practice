 
def minimum(arr):
    if len(arr) == 0:
        return None
    min = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min
    #your code here...
​
def maximum(arr):
    if len(arr) == 0:
        return None
    max = arr[0]
    for i in range(1,len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max
    #...and here