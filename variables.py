
#Note:
#1.python is a dynamically typed language, so we don't need to declare the type of a variable when we create it. The type is inferred from the value assigned to the variable.
#2.other programming languages like C, C++, Java, etc. are statically typed languages, so we need to declare the type of a variable when we create it.

my_number = 12               #automatically inferred as integer
my_string = "Hello, World!"  #automatically inferred as string 

## dynamic re binding of variable
x = 10        # x is currently an integer
x = "Python"  # x is now smoothly reassigned to a string
x = 3.14      # x is now smoothly reassigned to a float

## dynamic typing is a feature of Python that allows variables to change their type during runtime. 
print(x)


# 1. Variable ka basic syntax
# variable_name = value

name = "Vishal"  # variable name is 'name' and value is 'Vishal'
age = 22         # variable name is 'age' and value is 22
salary = 20000.50   # variable name is 'salary' and value is 20000.50

# 2. String variable
message = "Hello, Python!"  # variable name is 'message' and value is 'Hello, Python!'
print(message)  # output: Hello, Python!

# 3. Integer variable
number = 42  # variable name is 'number' and value is 42
print(number)  # output: 42

# 4. Boolean variable
is_active = True  # variable name is 'is_active' and value is True
print(is_active)  # output: True

# 5. List variable
fruits = ["apple", "banana", "cherry"]  # variable name is 'fruits' and value is a list of fruits
print(fruits)  # output: ['apple', 'banana', 'cherry']

# 6. Dictionary variable
person = {"name": "Vishal", "age": 22}  # variable name is 'person' and value is a dictionary with keys 'name' and 'age'
print(person)  # output: {'name': 'Vishal', 'age': 22}

# 7. Tuple variable
coordinates = (10.0, 20.0)  # variable name is 'coordinates' and value is a tuple with two float values
print(coordinates)  # output: (10.0, 20.0)

# A variable ke saath tum mainly 3 basic kaam karte ho:

# 1. Store a value
name = "vishal"
age = 22

# 2. Update a value
age = 23  # updating the value of age variable from 22 to 23
print(age)  # output: 23

# 3. Retrieve a value
print(name)  # output: vishal

# 1. Variable naming rules:
# - Variable names can contain letters, numbers, and underscores (_).
# - Variable names cannot start with a number.
# - Variable names are case-sensitive.  

