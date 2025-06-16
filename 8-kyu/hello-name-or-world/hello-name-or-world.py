def hello(name=""):
    name = name.strip()
    if not name:
        return "Hello, World!"
    return f"Hello, {name.capitalize()}!"
​