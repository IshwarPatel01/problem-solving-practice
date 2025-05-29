def persistence(n):
    count = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        count += 1
    return count
    
    
​
#     count = 0
#     while num >= 10:  # While number is not a single digit
#         product = 1
#         for digit in str(num):
#             product *= int(digit)
#         num = product
#         count += 1
#     return count
​