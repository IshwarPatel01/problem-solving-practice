def number(lines):
    #your code here
    n = 1
    arr = []
    if len(lines) == 0:
        return []
    for i in lines:
        result = f"{n}: {i}"
        arr.append(result)
        n += 1
    return arr