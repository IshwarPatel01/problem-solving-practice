def two_sort(array):
    # your code here
    array.sort()
    a = array[0]
    result = ""
    for char in a:
        result += char + "***"
    return result.rstrip("***")
        