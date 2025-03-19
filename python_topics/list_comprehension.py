# List comprehension example

# Squares of numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print("Even numbers:", evens)

# Create a list of uppercase characters from a string
word = "python"
upper_chars = [char.upper() for char in word]
print("Uppercase characters:", upper_chars)
