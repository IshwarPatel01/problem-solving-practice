def enough(cap, on, wait):
    # Your code here
    
    total_passenger =  cap - wait
    result = on - total_passenger
    return result