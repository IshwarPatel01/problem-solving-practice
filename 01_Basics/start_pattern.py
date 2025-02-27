# Crafting Star Patterns
# Difficulty: Easy
# Topics: Basic Programming, Patterns
# Description: Write a program to create different star patterns (e.g., pyramid, diamond).
# Example:
# Input: patternType = "pyramid", height = 5
# Output:
#     *
#    ***
#   *****
#  *******
# *********


def pyramid(height):
    for row in range(1, height + 1):
        spaces = " " * (height - row)
        stars = "*" * (2 * row - 1)
        print(spaces + stars)

# Example usage:
height = 5
pyramid(height)
