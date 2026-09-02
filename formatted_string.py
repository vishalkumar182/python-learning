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