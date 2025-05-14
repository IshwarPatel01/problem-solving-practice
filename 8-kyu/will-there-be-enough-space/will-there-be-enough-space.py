 
def enough(cap, on, wait):
    # Your code here
    
    total_passenger =  on + wait
    result = cap - total_passenger
    return abs(result)