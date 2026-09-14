## 1. What is a Dictionary?
#  A dictionary stores data in key-value pairs.

# example:

my_dict = {"name": "John", "age": 30, "city": "New York"}

student = {
    "name": "Vishal",
    "age": 22,
    "course": "BE CSE"
}


## syntax of dictionary:
# dictionary_name = {key1: value1, key2: value2, ...}


# 2. Why do we need Dictionary?

student = ["Vishal", 22, "BE CSE"]

# Problem: What does student[1] mean?
# print(student[1]) 

# problem with above list is that we have to remember the index of each value. 
# If we want to access the age, we have to remember that it is at index 1. 
# This can lead to confusion and errors.

# with dictionary, we can use descriptive keys to access values, making the code more readable and maintainable.
student = {
    "name": "Vishal",
    "age": 22,
    "course": "BE CSE"
}
print(student["age"])

# real world analogy:Imagine Instagram user data:
instagram_user = {
    "username": "john_doe",
    "email": "john@example.com",
    "followers": 1000
}
print(instagram_user["username"])

# Instead of remembering positions like 0, 1, 2, we use meaningful keys.

# 3. Creating a Dictionary
# most common way to create a dictionary is by using curly braces {} and separating keys and values with a colon :.
example = {
    "key1": "value1",
    "key2": "value2"
}

# empty dictionary can be created using empty curly braces {} or the dict() constructor.
empty_dict1 = {}
empty_dict2 = dict()

# later we can add key-value pairs to the dictionary using assignment.
empty_dict1["new_key"] = "new_value"


# 4. Key → Value important concept to understand.
student = {
    "name": "Vishal",
    "age": 22,
    "city": "Chennai"
}

# keys names are unique identifiers for values in a dictionary. Each key is associated with a specific value,
#  and you can use the key to access that value.

# note:A dictionary is primarily accessed using its keys.
student["name"] ## Output: 'Vishal'


# not by index like a list. If you try to access a value using an index, it will result in an error.
student[0]  # This will raise a KeyError

# 5. Accessing Values

student = {
    "name": "Vishal",
    "age": 22,
    "city": "Chennai"
}

# To access a value in a dictionary, you use the key associated with that value. 
# You can do this using square brackets [] or the get() method.

print(student["name"]) # accessing using square brackets
print(student.get("age")) # accessing using get() method


# note:
# 1. list uses index to access values, while dictionary uses keys.
# 2. If you try to access a key that doesn't exist using square brackets, it will raise a KeyError. 
# However, using the get() method will return None instead of raising an error.
# built-in data types in python are list, tuples, dictionary and set
