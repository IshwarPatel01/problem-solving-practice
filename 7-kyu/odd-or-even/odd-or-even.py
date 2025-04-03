def odd_or_even(arr):
    n = len(arr)
    if n <= 0 :
        return "even"
    sum = 0
    for i in range(n):
        sum += arr[i]
    if sum % 2 == 0:
        return "even"
    return "odd"