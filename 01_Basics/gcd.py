# Finding the Greatest Common Divisor (GCD)
# Difficulty: Easy
# Topics: Basic Programming, Number Theory
# Description: Write a program to find the GCD of two numbers.
# Example:
# Input: a = 48, b = 18
# Output: 6
# Explanation: The GCD of 48 and 18 is 6.


a=100
b= 25
while b > 0:
    a,b = b, a % b 
print(a)