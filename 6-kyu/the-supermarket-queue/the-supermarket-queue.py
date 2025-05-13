def queue_time(customers, n):
    time = [0] * n
    
    for c in customers:
        time[0] += c
        time.sort()
    return time[-1]