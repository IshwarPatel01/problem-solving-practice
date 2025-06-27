def reverse_letter(st):
    result = ""
    for char in range(len(st) - 1, -1, -1):
        if st[char].isalpha():
            result += st[char]
    return result