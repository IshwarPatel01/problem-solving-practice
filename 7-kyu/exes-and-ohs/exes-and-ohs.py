def xo(s):
    count = {"x" : 0 , "o": 0}
    
    for char in s.lower():
        if char == "x":
            count["x"] += 1
        elif char == "o":
            count ["o"] += 1
    return count["x"] == count["o"]