# input = integer n
# output = n should be multiple with both 3 and 7
# constraint = n can be negative, positive or zero

# take input integer "n"
# if n % 3 == 0 and n % 7 == 0
# print("n is multiple with both 3 and 7")
# else ("n is not multiple with both 3 and 7")

n = int(input())

if n % 3 == 0 and n % 7 == 0:
    print("n is multiple with both 3 and 7")
else:
    print("n is not multiple with both 3 and 7")

