 
def high_and_low(numbers):
    str_list = numbers.split()
    int_list = [int(x) for x in str_list]
    
    min_val = int_list[0]
    max_val = int_list[0]
    
    for num in int_list[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
            
    return f"{max_val} {min_val}"
​
   