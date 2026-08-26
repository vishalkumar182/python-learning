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