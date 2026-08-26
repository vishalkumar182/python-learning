# Input and output statement in python
# syntax of input statement
# variable_name = input("prompt message")

name = input("Enter your name: ")  # takes input from the user and assigns it to the variable 'name'
print("good morning:",name)

age = input("Enter your age: ")  # takes input from the user and assigns it to the variable 'age'
print("You are",age,"years old.")

# important note: input() function always returns a string, so if you want to take numerical input,
#  you need to convert it to the appropriate type (e.g., int or float) using type casting.

print(age)
print(type(age))  # this will show that the type of 'age' is <class 'str'>

converted_age = int(age)  # converting the string input to an integer
print(converted_age)
print(type(converted_age))  # this will show that the type of 'converted_age' is <class 'int'>

# example of taking float input
height = input("Enter your height in meters: ")  # takes input from the user and assigns it to the variable 'height'
converted_height = float(height)  # converting the string input to a float
print(converted_height)
print(type(converted_height))  # this will show that the type of 'converted_height' is <class 'float'>

# real world example: restaurant billing 
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("Total:", total)