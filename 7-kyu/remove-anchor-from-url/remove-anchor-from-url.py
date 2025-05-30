def remove_url_anchor(url):
    for i, char in enumerate(url):
        if char == "#":
            return url[:i]
    return url
​