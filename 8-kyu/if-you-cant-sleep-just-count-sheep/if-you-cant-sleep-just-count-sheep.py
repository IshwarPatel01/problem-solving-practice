def count_sheep(n):
    # your code
    if n == 0:
        return ""
    result = ""
    for i in range(1,n + 1):
        result += f"{i} sheep..."
        
    return result