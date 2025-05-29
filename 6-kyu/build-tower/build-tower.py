def tower_builder(n):
    width = 2 * n - 1
    return [('*' * (2 * i + 1)).center(width) for i in range(n)]
​