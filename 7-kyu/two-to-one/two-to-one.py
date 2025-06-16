def longest(a1, a2):
    a3 = a1 + a2
    
    result = ""
    for char in a3:
        if char not in result:
            result += char
    
    return "".join(sorted(result))