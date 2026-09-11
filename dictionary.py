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


