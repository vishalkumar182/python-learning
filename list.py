# list basic concepts

# problems with variables. ** variables can only store one value at a time **
from operator import index


name = "Vishal"
age = 23
salary = 25000

# But what if you have: 5 ememplyoees,10 products, 100 students, 1000 customers, 10000 users, 1000000 records, etc.
employee1 = "Vishal"
employee2 = "Rohit"
employee3 = "Priya"
employee4 = "Amit"
employee5 = "Sneha"
product1 = "Laptop"
product2 = "Mobile"
product3 = "Tablet"
product4 = "Watch"
product5 = "Headphones"
student1 = "John"
student2 = "Alice" 
student3 = "Bob"
student4 = "Charlie"
student5 = "David"
user1 = "user1"
user2 = "user2"
customer1 = "customer1"
customer2 = "customer2"
record1 = "record1"
record2 = "record2"

# creating a variable for each employee, product, student, user, customer, and record is not efficient and can lead to confusion.
# inorder to solve this problem, we can use a data structure called a list.
#  A list is a collection of values that can be of any data type. 
# Lists are mutable, meaning you can change their content without changing their identity.

employees = ["Vishal", "Rohit", "Priya", "Amit", "Sneha"]
products = ["Laptop", "Mobile", "Tablet", "Watch", "Headphones"]
students = ["John", "Alice", "Bob", "Charlie", "David"]
users = ["user1", "user2"]
customers = ["customer1", "customer2"]
records = ["record1", "record2"]



# If you want to store multiple values we cannot use a single variable.
# For example, if you want to store the names of multiple fruits, you cannot do it with a single variable. 
# You would need to create multiple variables for each fruit, which is not efficient and can lead to confusion.

fruit1 = "apple"
fruit2 = "banana"
fruit3 = "cherry"

# To solve this problem, Python provides a data structure called a list. 

fruits = ["apple", "banana", "cherry"] # single variable can store multiple values in a list.

# What is a List?
# a list is a collection used to store multiple values in a single variable.
# order of elements in a list is preserved, 
# meaning the order in which you add elements to a list is the order in which they will be stored and accessed.

# list can contain elements of different data types, including numbers, strings, and even other lists.
my_list = [1, "hello", 3.14, [1, 2, 3]]
print(my_list)  # output: [1, 'hello', 3.14, [1, 2, 3]]
marks = [90, 80, 70, 60, 50] # numbers
names = ["Vishal", "Rohit", "Priya", "Amit", "Sneha"] # strings
data = [1, "hello", 3.14, True, None] # mixed data types
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # list of lists (2D list)

# 1. Creating a list
# basic syntax of creating a list is to use square brackets [] and separate the elements with commas.
my_list = [1, 2, 3, 4, 5]
print(my_list)  # output: [1, 2, 3, 4, 5]

#empty list
empty_list = []
print(empty_list)  # output: []

# 2. Accessing elements
print(my_list[0])  # output: 1 (first element)
print(my_list[2])  # output: 3 (third element)
print(my_list[-1])  # output: 5 (last element)

# 3. Slicing
print(my_list[1:4])  # output: [2, 3, 4] (elements at indices 1, 2, 3)
print(my_list[:3])   # output: [1, 2, 3]
print(my_list[2:5])  # output: [3, 4, 5]

# 4. Modifying elements
my_list[0] = 10
print(my_list)  # output: [10, 2, 3, 4, 5]  


# 5. Adding elements
# append() method is used to add an element at the end of the list.
my_list.append(6)  # adds 6 at the end
print(my_list)  # output: [10, 2, 3, 4, 5, 6]

# insert() method is used to add an element at a specific index.
# syntax: list.insert(index, element)
my_list.insert(1, 15)  # adds 15 at index 1
print(my_list)  # output: [10, 15, 2, 3, 4, 5, 6]

# 6. Removing elements
# remove() method is used to remove the first occurrence of an element from the list.
my_list.remove(15)  # removes 15 from the list
print(my_list)  # output: [10, 2, 3, 4, 5, 6]

# pop() method is used to remove an element at a specific index and return it.
popped_element = my_list.pop(2)  # removes element at index 2 (which is 3) and returns it
print(popped_element)  # output: 3
print(my_list)  # output: [10, 2, 4, 5, 6]

#deleting an element by index using del keyword
del my_list[1]  # removes element at index 1 (which is 2)
print(my_list)  # output: [10, 4, 5, 6

# clearing the entire list using clear() method
my_list.clear()  # removes all elements from the list   

# 7. Length of a list
print(len(my_list))  # output: 4 (number of elements in the list)
