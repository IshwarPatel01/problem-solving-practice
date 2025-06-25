 
def solve(s):
    lowerCase = 0
    upperCase = 0
    
    for char in s:
        if char.islower():
            lowerCase += 1
        elif char.isupper():
            upperCase += 1
    
    if lowerCase > upperCase:
        result = s.lower()
    elif lowerCase < upperCase:
        result = s.upper()
    elif lowerCase == upperCase:
        result = s.lower()
    return result