def capitals(word):
    #your code here
    arr = []
    for i,char in enumerate(word):
        if char.isupper():
            arr.append(i)
    return arr
            