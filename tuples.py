numbers = (10, 20, 30, 40)
my_list = [10, 20, 30]
my_tuple = (10, 20, 30) 
fruits = ("apple", "banana", "mango")
print(fruits)
fruits = ("apple", "banana", "mango")

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])


# need of tuples 
# 1.


# tuples is defined using () and list is defined using []

numbers = (10, 20, 30, 40) # tuple
print(numbers[0])

numbers = [10, 20, 30, 40] # list
print(numbers[0])

# Tuples are immutable, meaning their elements cannot be changed after they are created. 
# Lists are mutable, meaning their elements can be changed.

# example of tuple immutability
fruits = ("apple", "banana", "mango")
# fruits[0] = "orange"  # This would raise an error since tuples are immutable
print(fruits)


# list is mutable
my_list = [10, 20, 30]
my_list[0] = 15
print(my_list)


# whn to use tuple and when to use list
# Use a tuple when you want to create a collection of items that should not change throughout the program. 
# Use a list when you want to create a collection of items that may change or be modified.

# real life example of tuple and list
# Tuple: A tuple can be used to represent a point in 2D space, where the x and y coordinates are fixed and should not change. For example, (3, 4) represents a point in 2D space.
# List: A list can be used to represent a collection of items that may change over time


# Tuples can be used as keys in dictionaries, while lists cannot. This is because tuples are hashable, while lists are not.
