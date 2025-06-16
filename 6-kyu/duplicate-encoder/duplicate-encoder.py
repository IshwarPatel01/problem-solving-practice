def duplicate_encode(word):
    result = ""
    
    freq = {}
    for char in word.lower():
        freq[char] = freq.get(char,0) + 1 
    for char in word.lower():
        if freq[char] == 1:
            result += "("
        else:
            result += ")"
    return result
        