 
def sum_str(a, b):
    if a == "" and b == "":
        return "0"
    elif a == "":
        return b
    elif b == "":
        return a
    else:
        result = int(a) + int(b)
        return str(result)
    