# ============================================================
# TYPE CONVERSION IN PYTHON
# ============================================================

# input() always returns the user's input as a STRING.
# Even if the user enters a number, Python stores it as text.


# ------------------------------------------------------------
# 1. WITHOUT int()
# ------------------------------------------------------------

l = input("Enter length: ")
b = input("Enter breadth: ")

print(type(l))   # <class 'str'>
print(type(b))   # <class 'str'>

# If you enter:
# l = "5"
# b = "4"

# Addition joins strings:
# "5" + "4" = "54"

# Multiplication between two strings is NOT allowed:
# "5" * "4" → TypeError


# ------------------------------------------------------------
# 2. USING int()
# ------------------------------------------------------------

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))

print(type(l))   # <class 'int'>
print(type(b))   # <class 'int'

# Now Python can perform mathematical calculations.

print(f"Area is {l * b}")

# Example:
# 5 * 4 = 20


# ------------------------------------------------------------
# 3. USING float() FOR DECIMAL NUMBERS
# ------------------------------------------------------------

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))

print(type(l))   # <class 'float'>
print(type(b))   # <class 'float'

print(f"Area is {l * b}")

# Example:
# 5.5 * 4.2 = 23.1


# ============================================================
# QUICK SUMMARY
# ============================================================

# input()  → String
# int()    → Integer
# float()  → Decimal number

# Remember:
# input() gives text.
# Use int() or float() when you need numbers.
# ============================================================