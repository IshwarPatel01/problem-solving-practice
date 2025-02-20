#input = int n 
#output = n is "divisible by 5 or not"
#constraint = integer can be positive, negative or zero

# take input integer "n"
# if n % 5 == 0
# print "divisible by 5"
# else "not divisible by 5"

n = int(input())

if n % 5 == 0:
    print("divisible by 5")
else:
    print("not divisible by 5")