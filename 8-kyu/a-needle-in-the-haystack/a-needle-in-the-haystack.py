def find_needle(haystack):
    for item in range(len(haystack)):
        if haystack[item] == "needle":
            return f"found the needle at position {item}"