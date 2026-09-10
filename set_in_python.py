# why do we need to use the set data structure in Python ?
# The set data structure in Python is used for several reasons:
# 1. To store unique elements only
# 2. For efficient membership testing
# 3. For mathematical operations like union, intersection, and difference



students = ["Vishal", "Rahul", "Amit", "Vishal", "Rahul"] # list with duplicate elements
unique_students = set(students) # convert list to set to remove duplicates
print(unique_students) # Output: {'Vishal', 'Rahul', 'Amit'}


# example of using set to store unique visitors to a website

visitors = {
    "Vishal",
    "Rahul",
    "Amit",
    "Vishal",
    "Rahul"
}

print(visitors) # remove duplicates and print unique visitors

print(len(visitors)) # print the number of unique visitors


# example
user_id={101,
         102,
         103,
         102,
         104,
         102,
         104,



}

unique_user_id=set(user_id) # convert list to set to remove duplicates
print(unique_user_id) # Output: {101, 102, 103, 104
print(len(unique_user_id)) # print the number of unique user ids


## Lesson 1 — The Problem Sets Solve

# A. uniqueness 
students = [
    "Vishal",
    "Rahul",
    "Amit",
    "Vishal",
    "Rahul",
    "Amit",
    "Vishal"
]  # list with duplicate elements
print("Total number of students:", len(students)) # Output: 7


unique_students = set(students)  # convert list to set to remove duplicates
print("Number of unique students:", len(unique_students)) # Output: 3



# B.membership testing
# Membership testing is the process of checking whether an element is present in a collection or not.
# example of using set to find unique employees in two companies



company_a = ["Vishal", "Rahul", "Amit", "Priya"]
company_b = ["Priya", "Amit", "John", "David"]


company_a_unique = set(company_a)
company_b_unique = set(company_b)

print("Unique employees in Company A:", company_a_unique)
print("Unique employees in Company B:", company_b_unique)

# Find common employees
common_employees = company_a_unique.intersection(company_b_unique)
print("Common employees:", common_employees)

# Find employees in either company
all_employees = company_a_unique.union(company_b_unique)
print("All employees:", all_employees)


#🚀 Now Lesson 2: What Exactly Is a Set?


my_list = [10, 20, 10, 30, 20]
my_set = {10, 20, 10, 30, 20}

print(my_list)
print(my_set)

# List → duplicates are allowed.
# Set → duplicate values are automatically collapsed.

# important points about sets in Python:
# 1. Sets are unordered collections of unique elements.


# One Important Property. 
# Sets are unordered collections.positional indexing is not possible.example of unordered collection
my_set = {10, 20, 30, 40}
print(my_set)
print(my_set[0])  # This will raise an error since sets are unordered and do not support indexing.


# Lesson 3 — Creating Sets
# 1. Using curly braces {}
my_set = {1, 2, 3, 4, 5}
print(my_set)

# 2. Using the set() constructor
my_set = set([1, 2, 3, 4, 5])
print(my_set)

numbers = [10, 20, 10, 30, 20]
unique_numbers = set(numbers)
print(unique_numbers)


## ⚠️ VERY IMPORTANT: Empty Set Trap
empty_set = {}  # This creates an empty dictionary, not a set
print(type(empty_set))  # Output: <class 'dict'>

empty_set = set()  # This creates an empty set
print(type(empty_set))  # Output: <class 'set'>

## We can use a set to quickly get unique values from data and remove duplicates.
customer_ids = [101, 102, 101, 103, 102, 104]

unique_customers = set(customer_ids)

print(unique_customers)
print(len(unique_customers))

#One More Important Concept: set() Can Convert Different Collections . This is where set() becomes more powerful.

# from list to set
my_list = [1, 2, 3, 4, 5, 1, 2, 3]
my_set = set(my_list)
print(my_set)

# from tuple to set
my_tuple = (1, 2, 3, 4, 5, 1, 2, 3)
my_set = set(my_tuple)
print(my_set)

# from string to set
my_string = "hello world"  
my_set = set(my_string)
print(my_set)

# from dictionary to set
my_dict = {"a": 1, "b": 2, "c": 3}
my_set = set(my_dict)
print(my_set)

# from range to set
my_range = range(1, 6)
my_set = set(my_range)
print(my_set)

# from set to set
my_set1 = {1, 2, 3, 4, 5}
my_set2 = set(my_set1)
print(my_set2)

# Note:"A set stores unique elements, so duplicate values are automatically removed"


# Lesson 4 — Adding and Removing Elements

# 1. Adding elements to a set :
# use the add() method to add a single element to a set. 
# If the element already exists, it will not be added again.

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")  # add a single element
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}


fruits = {"apple", "banana"}
fruits.add("apple")
print(fruits)  # Output: {'apple', 'banana'}

# 2.Adding multiple elements to a set:
# use the update() method to add multiple elements to a set.

fruits = {"apple", "banana", "cherry"}
fruits.update(["orange", "grape"])
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange', 'grape'}   

#    OR
fruits = {"apple", "banana", "cherry"}
fruits.update(("orange", "grape"))
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange', 'grape'}   

# 3. Removing elements from a set:

# use the remove() method to remove a specific element from a set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry'}

# use the discard() method to remove a specific element from a set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)  # Output: {'apple', 'cherry'}

# use the pop() method to remove and return an arbitrary element from a set.
fruits = {"apple", "banana", "cherry"}
removed_fruit = fruits.pop()
print(removed_fruit)  # Output: (arbitrary element from the set)
print(fruits)  # Output: (set with the arbitrary element removed)

# use the clear() method to remove all elements from a set.
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)  # Output: set()

# use the del keyword to delete a set entirely.
fruits = {"apple", "banana", "cherry"}
del fruits

# remove() vs discard() vs pop() vs clear() vs del
# remove() - removes a specific element from the set. Raises KeyError if the element is not found.
# discard() - removes a specific element from the set. Does not raise an error if the element is not found.
# pop() - removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.
# clear() - removes all elements from the set, leaving it empty.    

# to remove multiple elements from a set, you can use the difference_update() method or the intersection_update() method.


