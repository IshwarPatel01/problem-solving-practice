def accum(st):
    result = ""
    for i, char in enumerate(st):
        result += char.upper() + char.lower() * i + "-"
    return result.rstrip("-")
        