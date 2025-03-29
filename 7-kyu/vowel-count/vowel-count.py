def get_count(sentence):
    count = 0
    
    dict = {}
    
    if sentence == "":
        return 0
    
    for char in sentence:
        dict[char] = dict.get(char,0) + 1
    
    for char in dict:
            if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
                count += dict[char]
         
                
    return count