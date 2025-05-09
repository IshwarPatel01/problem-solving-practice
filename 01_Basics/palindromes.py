# Identifying Palindromes
# Difficulty: Easy
# Topics: Basic Programming, String Manipulation
# Description: Write a program to check if a string or number is a palindrome.
# Example:
# Input: string = "radar"
# Output: Palindrome
# Explanation: "radar" reads the same backward as forward.




s1 = "radar"

def check_palindrome(s1):
    return s1 == s1[::-1]

print(check_palindrome(s1))