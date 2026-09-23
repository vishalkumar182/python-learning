

# need of functions in python:

# 1. Reusability: Functions allow you to write a block of code once and reuse
# it multiple times throughout your program. This reduces code duplication and makes your code more organized.

# 2. Modularity: Functions help break down complex problems into smaller, manageable pieces.
# Each function can focus on a specific task, making it easier to understand and maintain the code.

# 3. Readability: Functions can improve the readability of your code by giving meaningful names to blocks of code. 
# This makes it easier for others (and yourself) to understand what the code does.

# example:
name = "Vishal"
print("Hello, " + name + "!") 
name = "John"
print("Hello, " + name + "!")
name = "Alice"
print("Hello, " + name + "!")

# instead of repeating the same code, we can define a function to greet a user:
def greet_user(name):
    print("Hello, " + name + "!")

greet_user("Vishal")
greet_user("John")
greet_user("Alice")


# creating a function in python:
# use the def keyword followed by the function name and parentheses ().

def function_name(parameters):
    # code block
    return   # optional


def is_even(number):
    """Returns True if a number is even, False otherwise."""
    return number % 2 == 0

# Test the function
print(is_even(7))   # Output: False
print(is_even(12))  # Output: True

def celsius_to_fahrenheit(celsius):
    """Converts Celsius temperatures to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage
current_temp = celsius_to_fahrenheit(25)
print(f"25°C is equal to {current_temp}°F")  # Output: 25°C is equal to 77.0°F


def calculate_area(length, width):
    """Returns the area of a rectangle."""
    return length * width

# Test the function
result = calculate_area(5, 10)
print(f"The area is: {result}")  # Output: The area is: 50

def find_max_of_three(a, b, c):
    """Finds the maximum of three values manually."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Test the function
print(find_max_of_three(15, 42, 9))  # Output: 42

