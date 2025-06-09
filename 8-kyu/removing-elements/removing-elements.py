 
def remove_every_other(arr):
    result = []
    for item in range(len(arr)):
        if item % 2 == 0:
            result.append(arr[item])
    return result
​