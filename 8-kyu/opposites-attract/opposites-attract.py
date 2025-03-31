def lovefunc( flower1, flower2 ):
    odd = 0
    even = 0
    
    if flower1 % 2 == 0 or flower2 % 2 == 0:
        even = 1
    if flower1 % 2 == 1 or flower2 % 2 == 1:
        odd = 1
    if even == odd:
        return True
    else:
        return False
        
    
    # ...