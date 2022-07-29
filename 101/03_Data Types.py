# Data Types

# Text Type - str
# Numeric Types - int, float, complex
# Sequence Types - list, tuple, range
# Mapping Type - dict
# Set Types - set, frozenset
# Boolean Type - bool
# Binary Types - bytes, bytearray, memoryview
# None Type - NoneType

##############################################################################

# Getting The Data Type
x = 5
print(type(x)) #<class 'int'>

##############################################################################
x = "Zeus"
print(x)
print(type(x)) #<class 'str'>
##############################################################################
x = 20
print(x)
print(type(x)) #<class 'int'>
##############################################################################
x = 20.5
print(x)
print(type(x)) #<class 'float'>
##############################################################################
x = 3+5j
print(x)
print(type(x)) #<class 'complex'>
##############################################################################
x = [1,2,3,4,5]
print(x)
print(type(x)) #<class 'list'>
##############################################################################
x = ("Zeus", "Slayer", "Odin")
print(x)
print(type(x)) #<class 'tuple'>
##############################################################################
x = range(10)
print(x)
print(type(x)) #<class 'range'>
##############################################################################
x = {"Zeus": "Slayer", "Odin": "Thor"}
print(x)
print(type(x)) #<class 'dict'>
##############################################################################
x = {"Zeus", "Slayer", "Odin"}
print(x)
print(type(x)) #<class 'set'>
##############################################################################
x = frozenset(["Zeus", "Slayer", "Odin"])
print(x)
print(type(x)) #<class 'frozenset'>
##############################################################################
x = True
print(x)
print(type(x)) #<class 'bool'>
##############################################################################
x = b"Zeus"
print(x)
print(type(x)) #<class 'bytes'>
##############################################################################
x = bytearray(5)
print(x)
print(type(x)) #<class 'bytearray'>
##############################################################################
x = memoryview(bytes(5))
print(x)
print(type(x)) #<class 'memoryview'>
##############################################################################
x = None
print(x)
print(type(x)) #<class 'NoneType'>
##############################################################################
