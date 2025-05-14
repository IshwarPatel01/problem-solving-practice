 
def rental_car_cost(d):
    total_amt = 0
    if d >= 7:
        total_amt = (40 * d) - 50
    elif d >= 3:
        total_amt = (40 *d) - 20
    else:
        total_amt = 40 * d
    return total_amt