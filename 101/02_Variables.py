#variables
x = 5
y = "Hello World"
print(x)
print(y)
y = 23
print(y)

#############################################################################

#Casting
x = str(3)
y = int(3)
z = float(3)
print(x,y,z)

#############################################################################

#Get the Type
x = 5
y = "Zeus"
print(type(x))
print(type(y))

#############################################################################

#Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print(x) #Orange
print(y) #Banana
print(z) #Cherry

x = y = z = "Orange"
print(x) #Orange
print(y) #Orange
print(z) #Orange

#############################################################################

#Unpacking
fruits = ["Apple", "Banana", "Cherry"]
x, y, z = fruits
print(x) #Apple
print(y) #Banana
print(z) #Cherry
print(fruits) #["Apple", "Banana", "Cherry"]

#############################################################################

#Output
x = "Zeus"
y = "Slayer"
print(x + " " + y) #Zeus Slayer

x = 5
y = 6
print(x + y) #11

x = 5
y = "Zeus"
print(x , y) #5 Zeus

#############################################################################

#Global Variables
x = "Zeus"

def foo():
    print(x + "Slayer")

foo()


x = "awesome"

def myfunc():
    #local variable
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc2():
    global x
    x = "fantastic"

myfunc2()
print("Python is " + x)