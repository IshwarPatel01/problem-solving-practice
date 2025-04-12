def is_pangram(st):
    dict = {}
    for char in st.lower():
        if char.isalpha():
            item = (ord(char) - ord("a")) + 1
            dict[item] = 1
    if len(dict) == 26:
        return True
    else:
        return False