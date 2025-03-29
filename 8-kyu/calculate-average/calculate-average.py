def find_average(numbers):
    # your code here
    if not numbers:
        return 0
    count = 0
    n = len(numbers)
    
    for i in numbers:
        count += i
    
    return count / n
    