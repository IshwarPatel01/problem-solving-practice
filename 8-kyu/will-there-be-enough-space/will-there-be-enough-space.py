def enough(cap, on, wait):
    # Your code here
    total_passenger = on + wait
    if cap >= total_passenger:
​
        return 0
    else:
        return abs(cap - total_passenger)