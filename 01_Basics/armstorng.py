# Calculating Armstrong Numbers
# Difficulty: Easy
# Topics: Basic Programming, Number Theory
# Description: Write a program to check if a number is an Armstrong number.
# Example:
# Input: number = 153
# Output: Armstrong Number
# Explanation: 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153


n = 13

def armstrong_num(n):
    temp = n
    total = 0
    digits = len(str(n))

    while temp > 0:
        digit = n % 10
        total +=  digit ** digits
        temp //= 10
    
    return total == n

print(armstrong_num(n))