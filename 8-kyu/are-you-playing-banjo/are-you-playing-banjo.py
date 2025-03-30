def are_you_playing_banjo(name):
    i = name[0]
    result = ""
    if i == "R" or i == "r":
        result = name + " plays banjo"
    else:
        result = name + " does not play banjo"
    return result