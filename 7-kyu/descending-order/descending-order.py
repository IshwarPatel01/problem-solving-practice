def descending_order(num):
    num_str = list(str(num))
    num_str.sort()
    result = ""
    n = len(num_str)
    for i in range(n-1,-1,-1):
        result += num_str[i]
    return int(result)
    # Bust a move right here