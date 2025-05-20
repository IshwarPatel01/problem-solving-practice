def count(s):
    if s == "":
        return {}
    
    count = {}
    
    for char in s:
        count[char] = count.get(char,0) + 1
    return count