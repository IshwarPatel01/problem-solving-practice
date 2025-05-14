 
def enough(cap, on, wait):
    # Your code here
    
    total_passenger =  on + wait
    result = total_passenger - cap
    return abs(result)