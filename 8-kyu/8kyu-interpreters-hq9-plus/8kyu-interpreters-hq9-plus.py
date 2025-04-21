def HQ9(code):
    if code == 'H':
        return "Hello World!"
    elif code == 'Q':
        return code
    elif code == '9':
        result = []
        for i in range(99, 0, -1):
            result.append(f"{i} bottle{'s' if i != 1 else ''} of beer on the wall, {i} bottle{'s' if i != 1 else ''} of beer.")
            if i - 1 > 0:
                result.append(f"Take one down and pass it around, {i - 1} bottle{'s' if i - 1 != 1 else ''} of beer on the wall.")
            else:
                result.append("Take one down and pass it around, no more bottles of beer on the wall.")
        result.append("No more bottles of beer on the wall, no more bottles of beer.")
        result.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
        return '\n'.join(result)
    else:
        return None  # or empty string, depending on how Codewars wants it
​