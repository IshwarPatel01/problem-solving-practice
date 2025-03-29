def reverse_words(text):
    
    result = ""
    word = ""
    for char in text:
        if char == " ":
            result += word[::-1] + " "
            word = ""
        else:
            word += char
    result += word[::-1]
    return result