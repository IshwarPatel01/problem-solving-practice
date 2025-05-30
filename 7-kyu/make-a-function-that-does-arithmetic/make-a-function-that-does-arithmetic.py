 
def arithmetic(a, b, operator):
    operators = {
        "add" : a + b,
        "subtract" : a - b,
        "multiply" : a * b,
        "divide" : a / b
    }
    return operators[operator]