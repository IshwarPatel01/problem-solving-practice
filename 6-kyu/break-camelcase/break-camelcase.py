 
def solution(s):
    
    for char in range(len(s)):
        if s[char].isupper():
            upper_len = char
    val1 = s[:upper_len]
    val2 = s[upper_len:]
    return f"{val1} {val2}"
​
        
        
    