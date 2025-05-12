 
def remove_char(s):
    n = len(s)
    result = ""
    for char in range(1,n-1):
        result += s[char]
    return result