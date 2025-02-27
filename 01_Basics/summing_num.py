# Summing Digits of a Number
# Difficulty: Easy
# Topics: Basic Programming, Mathematical Computations
# Description: Write a program to calculate the sum of digits of a number.
# Example:
# Input: number = 1234
# Output: 10
# Explanation: The sum of the digits 1 + 2 + 3 + 4 = 10.

n = 1234
total = 0
temp = n

while temp > 0:
    digit =  temp % 10
    total += digit
    temp //= 10

print(total)
