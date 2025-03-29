def validate_pin(pin):
    
    n = len(pin)
​
    if pin.isnumeric():
        if n == 4 or n == 6:
            return True
   
    return False
    # return true or false