def count_positives_sum_negatives(arr):
    if not arr:
        return []
    
    count = 0
    sum_neg = 0
    for n in arr:
        if n < 0:
            sum_neg += n
        elif n > 0:
            count += 1
    return [count, sum_neg]
            
            
    
    