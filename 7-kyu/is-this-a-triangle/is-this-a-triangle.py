def is_triangle(a, b, c):
    if (a + b) > c and (a+c) > b and (b + c) > a:
        return True
    return False
# a + b > c
# a + c > b
# b + c > a
​