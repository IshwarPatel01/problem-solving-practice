# input = integer n
# output = check n is leap year or not
# constraints = n should be 4 digit to check leap year / n not should be negative and zero it should be positive 

# take input int "n"
# if n % 400 == 0 
# print("true")
# elif n % 100 == 0
#  print("false")
# elif n % == 4:
# print ("true")


# but we have to find 4 digit leap year
# take input int "n"
# if n % 4 == 0
# print("true")
# else false 

n = int(input())

if n % 400 == 0:
    print("leap year")
elif n % 100 == 0:
    print("not leap year")
elif n % 4 == 0:
    print("leap year")
else:
    print("not leap year")

    