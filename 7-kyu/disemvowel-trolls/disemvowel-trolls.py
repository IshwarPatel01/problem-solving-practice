 
def disemvowel(string_):
    vowels_list = ["a","A","E","e","i","I","o","O","u","U"]
#     vowels_list = ["a","e","i","o","u"]    
    result = ""
    for char in string_:
        if char not in vowels_list:
            result += char
        
    
    return result