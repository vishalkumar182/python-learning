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