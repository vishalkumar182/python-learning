# String basic Concepts
# Simple definition: A string is a sequence of characters enclosed in quotes. Characters can be letters, numbers, symbols, or whitespace.

# important point
age = 25 # age is an integer
age = "25"  # age is now a string
print(age)  # output: 25
print(type(age))  # output: <class 'str'>

# 2. how do python know its a string?
# Python knows it's a string because it is enclosed in quotes.

# 3. String can be declared using single quotes, double quotes, or triple quotes.

single_quote_string = 'Hello, World!'
double_quote_string = "Hello, World!"
triple_quote_string = '''Hello, World!'''
print(single_quote_string)
print(double_quote_string)
print(triple_quote_string)  

# 4. string can be words, sentences, or even paragraphs.or numbers or special characters.
word = "Python"
sentence = "I love programming in Python."
paragraph = """This is a paragraph.
It has multiple lines."""
print(word)
print(sentence)
print(paragraph)

name = "Vishal"
city = "Chennai"
message = "Hello World"
phone = "9876543210"
age = "23"
price = "499"
 
# 5. String can contain spaces, special characters, and numbers.
string_with_spaces = "Hello, how are you?"
string_with_special_chars = "Hello, @#$%^&*()!"

# 6. String can be empty or contain only whitespace.
empty_string = ""
print(len(empty_string))  # output: 0
whitespace_string = "   "
print(len(whitespace_string))  # output: 3

# Strings operations
# 1. Concatenation: Joining two or more strings together using the + operator.
# 2. Repetition: Repeating a string multiple times using the * operator.
# 3. Indexing: Accessing individual characters in a string using their index (position).
# 4. Slicing: Extracting a portion of a string using a range of indices
# 5. Length: Getting the number of characters in a string using the len() function.
# 6. Membership: Checking if a substring exists within a string using the in operator.
# 7. String formatting: Inserting values into a string using placeholders or f-strings.
# 8. Escape sequences: Using special characters to represent certain actions or characters within a string (e.g., \n for newline, \t for tab).
# 9. String methods: Using built-in functions to manipulate and transform strings (e.g., upper(), lower(), strip(), replace(), split(), join()).
# 10. String immutability: Strings in Python are immutable, meaning their values cannot be changed after they are created. Any operation that modifies a string will create a new string instead of modifying the original one.

# 1. Concatenation
first_name = "Vishal"
last_name = "Sharma"
full_name = first_name + " " + last_name
print(full_name)  # output: Vishal Sharma

# 2. Repetition
greeting = "Hello! "
print(greeting * 3)  # output: Hello! Hello! Hello!

# 3. Indexing
text = "Python"
print(text[0])  # output: P
print(text[1])  # output: y 
print(text[-1])  # output: n (last character)
print(text[-2])  # output: o (second last character)

# 4. Slicing
print(text[0:3])  # output: Pyt (characters at indices 0, 1, 2)
print(text[2:5])  # output: tho (characters at indices 2, 3, 4)
print(text[:3])   # output: Pyt (characters from the beginning up to index 3)
print(text[3:6])  # output: hon (characters from index 3 up to index 6)

# 5. Length
print(len(text))  # output: 6

# 6. Membership
print("Py" in text)  # output: True
print("Java" in text)  # output: False

# 7. String formatting
name = "Vishal"
age = 23
message = f"Hello, my name is {name} and I am {age} years old."
print(message)  # output: Hello, my name is Vishal and I am 23 years old.

# 8. Escape sequences
print("Hello\nWorld")  # output: Hello (newline) World
print("Hello\tWorld")  # output: Hello (tab) World  


# 9. String methods
text = "  Hello, World!  "
print(text.upper())  # output:   HELLO, WORLD!  
print(text.lower())  # output:   hello, world!  
print(text.strip())  # output: Hello, World!
print(text.replace("Hello", "Hi"))  # output:   Hi, World!
print(text.split(","))  # output: ['  Hello', ' World!  ']  
print(",".join(text.split(",")))  # output:   Hello, World!  

# 10. String immutability
original_string = "Hello"
new_string = original_string.upper()
print(original_string)  # output: Hello
print(new_string)  # output: HELLO

# converting string to list
string = "Hello, World!"
char_list = list(string)
print(char_list)  # output: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']

# converting list to string
char_list = ['H', 'e', 'l', 'l', 'o', ',',  ' ', 'W', 'o', 'r', 'l', 'd', '!']
string = ''.join(char_list)
print(string)  # output: Hello, World!  

# string to integer
string_number = "123"   
integer_number = int(string_number)
print(integer_number)  # output: 123

# integer to string
integer_number = 456
string_number = str(integer_number)
print(string_number)  # output: 456 

