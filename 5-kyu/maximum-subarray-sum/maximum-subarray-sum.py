def max_sequence(arr):
    
#     max_sum = 0
#     n = len(arr)
    
#     for i in range(n):
#         current_sum = 0
#         for j in range(i,n):
#             current_sum += arr[j]
#             if max_sum < current_sum:
#                 max_sum = current_sum
    
#     return max_sum
    max_sum = 0
    current_sum = 0
    
    for item in arr:
        if current_sum + item > 0:
            current_sum += item
        else:
            current_sum = 0
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
        