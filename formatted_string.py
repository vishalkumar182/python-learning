# formatted string in python

# basic idea

# normal string
print("Hello Vishal") # hardcoded string

# value come from variable
name = "VISHAL KUMAR"
print("My name is " + name) # concatenation of string and variable

# taking input from user
name = input("Enter your name: ")
print("My name is " + name) # concatenation of string and variable

# better way to format string using f-string
# syntax: f"string {variable}"
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"My name is {name} and I am {age} years old.") # using f-string to format string with variables

# without f-string
name = input("Enter your name: ")
age = input("Enter your age: ")
print("My name is {} and I am {} years old.".format(name, age)) # using format() method to format string with variables

l = int(input("enter length:"))
b = int(input("enter breadth:"))
print(f"area is {l*b}")

# ============================================================
# FORMATTED STRINGS IN PYTHON
# ============================================================

# A formatted string allows us to easily combine:
# 1. Normal text
# 2. Variables
# 3. Calculated values
#
# The most common and recommended way is using an f-string.


# ============================================================
# 1. NORMAL STRING
# ============================================================

# A normal string contains fixed text.

print("Hello Vishal")

# Output:
# Hello Vishal


# ============================================================
# 2. STRING + VARIABLE
# ============================================================

# We can store a value inside a variable
# and then use that variable in a string.

name = "VISHAL KUMAR"

print("My name is " + name)

# Output:
# My name is VISHAL KUMAR


# ============================================================
# 3. TAKING VALUE FROM USER
# ============================================================

# input() takes a value from the user.
# By default, input() returns a string.

name = input("Enter your name: ")

print("My name is " + name)

# Example:
# Enter your name: Vishal
# My name is Vishal


# ============================================================
# 4. PROBLEM WITH CONCATENATION
# ============================================================

# When we have multiple variables,
# using + can become difficult to read.

name = input("Enter your name: ")
age = input("Enter your age: ")

print("My name is " + name + " and I am " + age + " years old.")

# This works, but the code becomes lengthy
# when we have many variables.


# ============================================================
# 5. F-STRING — BETTER WAY
# ============================================================

# An f-string allows us to directly place variables
# inside a string.

# Syntax:
#
# f"Text {variable}"


name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"My name is {name} and I am {age} years old.")

# Example:
# Enter your name: Vishal
# Enter your age: 23
#
# Output:
# My name is Vishal and I am 23 years old.


# ============================================================
# 6. F-STRING WITH MULTIPLE VARIABLES
# ============================================================

name = "Vishal"
age = 23
city = "Chennai"

print(f"My name is {name}, I am {age} years old, and I live in {city}.")

# Output:
# My name is Vishal, I am 23 years old, and I live in Chennai.


# ============================================================
# 7. F-STRING WITH CALCULATIONS
# ============================================================

# We can also perform calculations inside { }.

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))

print(f"Area is {l * b}")

# Example:
# Enter length: 5
# Enter breadth: 4
#
# Output:
# Area is 20


# ============================================================
# 8. F-STRING WITH EXPRESSIONS
# ============================================================

# Anything that produces a value can generally
# be placed inside { }.

a = 10
b = 5

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")

# Output:
# Addition: 15
# Subtraction: 5
# Multiplication: 50
# Division: 2.0


# ============================================================
# 9. USING .format()
# ============================================================

# Before f-strings, Python commonly used the .format() method.

name = "Vishal"
age = 23

print("My name is {} and I am {} years old.".format(name, age))

# Output:
# My name is Vishal and I am 23 years old.


# ============================================================
# 10. F-STRING vs .format()
# ============================================================

name = "Vishal"
age = 23

# Using f-string
print(f"My name is {name} and I am {age} years old.")

# Using .format()
print("My name is {} and I am {} years old.".format(name, age))

# Both produce the same output.
#
# f-string is generally preferred because it is:
# - Easier to read
# - Shorter
# - Easier to maintain


# ============================================================
# 11. F-STRING WITH DIFFERENT DATA TYPES
# ============================================================

name = "Vishal"       # string
age = 23              # integer
height = 5.8          # float
is_student = True     # boolean

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Student: {is_student}")


# ============================================================
# 12. IMPORTANT SYNTAX
# ============================================================

# f-string:
#
# f"Hello {name}"
#
#        ↑
#     variable
#
# The 'f' before the string tells Python:
# "This string contains values that need to be replaced."


# ============================================================
# QUICK SUMMARY
# ============================================================

# Normal string:
# print("Hello Vishal")

# String concatenation:
# print("My name is " + name)

# f-string:
# print(f"My name is {name}")

# .format():
# print("My name is {}".format(name))


# ============================================================
# KEY TAKEAWAY
# ============================================================

# Use f-strings when you want to combine
# text with variables or calculations.

# Recommended:
#
# print(f"My name is {name} and I am {age} years old.")
#
# f-string = f"Text {value}"
# ============================================================