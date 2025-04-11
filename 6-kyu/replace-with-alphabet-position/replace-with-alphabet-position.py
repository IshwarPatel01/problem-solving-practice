def alphabet_position(text):
    result = ""
    for char in text.lower():
        if char.isalpha():
            result += str(ord(char) - ord("a") + 1) + " "
    return result.strip()
    
    
#     result = ""
#     letters = ""
#     for char in text.lower():
#         if char.isalpha():
#             letters += char
    
#     for char in letters:
#         result += str(ord(char) - ord("a") + 1) + " "
#     return result.strip()
        
​
   
​
​
​
​
​
​