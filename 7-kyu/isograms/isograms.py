def is_isogram(string):
    if string == "":
        return True
    s = string.lower()
    count = 0
    seen = set()
    
    for char in s:
        if char in seen:
            count = 1
        seen.add(char)
    if count == 0:
        return True
    else:
        return False
​
        
        
#your code here