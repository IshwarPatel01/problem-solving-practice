# Finding the Factorial of a Number
# Difficulty: Easy
# Topics: Basic Programming, Mathematical Computations
# Description: Write a program to compute the factorial of a given number.
# Example:
# Input: number = 5
# Output: 120
# Explanation: 5! (factorial) is 5 × 4 × 3 × 2 × 1 = 120.


n = 5 
fact = 1

for i in range(1,n + 1):
    fact *= i

print(fact)
