print("Hello") # and
print("World") # are the same thing

# Assign a string to a variable
a = "Hello"
b = "World"
c = """Hello
Zeus"""
print(a + " " + b + " " + c)

# Strings are arrays
a = "Hello World"
print(a[0]) # prints H

# Looping through a string
for x in "Zeus":
    print(x) # prints each character in the string

# String length
a = "Hello World"
print(len(a)) # prints 11

#Check String
txt = "There are no gods in the heavens"

print("gods" in txt) # returns True
print("Zeus" not in txt) # returns True

if "gods" in txt:
    print("Yes, gods is in the text") # prints Yes, gods is in the text

###############################################################################

# Slicing a String

a = "Hello World"
print(a[2:5]) # prints "llo"

# Slicing a string from the start
print(a[:5]) # prints "Hello"

# Slicing a string to the end
print(a[2:]) # prints "llo World"

# Negative indexing
print(a[-5:-2]) # prints "Wor"

###############################################################################

# Modify a String

# Uppercase
a = "Hello World"
print(a.upper()) # prints "HELLO WORLD"

# Lowercase
a = "Hello World"
print(a.lower()) # prints "hello world"

# Remove whitespace
a = " Hello World     "
print(a.strip()) # prints "Hello World"

# Replace text
a = "Hello World"
print(a.replace("World", "Universe")) # prints "Hello Universe"

# Split a string into a list
a = "Zeus, Poseidon, Hades"
print(a.split(",")) # prints ["Zeus", "Poseidon", "Hades"]

###############################################################################

# String Concatenation

a = "Hello"
b = "World"
c = a + " " + b
print(c) # prints "Hello World"

###############################################################################

# String Formatting

# The "format()" method takes the passed arguments, formats them, 
# and places them in the string where the placeholders "{}" are:

age = 23
txt = "My name is Zeus, and I am"
# print(txt + age) # can't concatenate a string and an integer

age = 23
txt = "My name is Zeus, and I am {} years old"
print(txt.format(age)) # prints "My name is Zeus, and I am 23 years old"

quantity = 2
itemno = 12345
price = 1.99
myorder = "I want {} pieces of item number {} for {} dollars."
print(myorder.format(quantity, itemno, price)) # prints "I want 2 pieces of item number 12345 for 1.99 dollars."

quantity = 2
itemno = 12345
price = 1.99
myorder = "I want {2} pieces of item number {0} for {1} dollars."
print(myorder.format(quantity, itemno, price)) # prints "I want 1.99 pieces of item number 2 for 12345 dollars."

###############################################################################

# Escape characters

# The "\" character is used to escape special characters in a string. Just use the link below for more information:
# https://www.w3schools.com/python/python_strings_escape.asp

###############################################################################

# String Methods

# All string methods return a new string. They do not change the original string.
# https://www.w3schools.com/python/python_strings_methods.asp
