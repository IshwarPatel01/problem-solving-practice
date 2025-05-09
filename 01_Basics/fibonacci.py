# Generating the Fibonacci Series
# Difficulty: Easy
# Topics: Basic Programming, Sequences
# Description: Write a program to generate the Fibonacci series up to a given number.
# Example:
# Input: limit = 10
# Output: [0, 1, 1, 2, 3, 5, 8]
# Explanation: The Fibonacci series up to 10 is generated as [0, 1, 1, 2, 3, 5, 8].

n= 10

fib = [0,1]

while fib[-1] + fib[-2] < n:
    fib.append(fib[-1] + fib[-2])
print(fib)