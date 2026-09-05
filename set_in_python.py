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