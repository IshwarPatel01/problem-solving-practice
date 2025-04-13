def order(sentence):
    if sentence == "":
        return ""
    
    words = sentence.split()
    
    def get_number(words):
        for char in words:
            if char.isdigit():
                return int(char)
    words.sort(key = get_number)
    return " ".join(words)