def positive_sum(arr):
    # Your code here
    total_sum = 0
    for i in arr:
        if i > 0:
            total_sum += i
    
    if total_sum == 0:
        return 0
    else:
        return total_sum
​