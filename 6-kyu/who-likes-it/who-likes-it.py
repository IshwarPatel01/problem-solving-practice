 
def likes(names):
    # your code here
    n = len(names)
    
    if n == 0:
        return "no one likes this"
    elif n == 1:
        return f"{names[0]} likes this"
    elif n == 2:
        return f"{names[0]} and {names[1]} like this"
    elif n == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        max_names = n - 2
        return f"{names[0]}, {names[1]} and {max_names} others like this"