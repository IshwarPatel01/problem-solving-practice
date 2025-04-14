def sort_array(source_array):
    arr = source_array
    odd_numbers = []
    
    # Extract the odd numbers from the array
    for num in arr:
        if num % 2 != 0:
            odd_numbers.append(num)
    
    # Sort the odd numbers
    odd_numbers.sort()
    
    # Create a result list to place the sorted odd numbers back
    result = []
    odd_index = 0
    
    for num in arr:
        if num % 2 != 0:
            result.append(odd_numbers[odd_index])
            odd_index += 1
        else:
            result.append(num)
    
    return result