#python syntax
print("Hi World")

#identation, Python uses indentation to indicate a block of code. Click tab
if 5 > 2:
    print("five is greater than two")

#variables
x = "selamat malam"
y = 20
print(x)
print(y)

#Casting
x = str(3)
y = float(3)
z = int(3)
print(x)
print(y)
print(z)

#printing type
x = 20
y = "Yudha"
z = 4.3
print(type(x))
print(type(y))
print(type(z))

#multiple values to multiple varibales
x, y, z = "Yudha", "Farizky", "Ramanda"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Yudha Farizky Ramanda"
print(x)
print(y)
print(z)

#unpack collection
name = ["Yudha", "Farizky", "Ramanda"]
a, b, c = name
print(a)
print(b)
print(c)

#output variables
a = "Yudha Farizky Ramanda"
print(a)

#output variables pakai koma
a = "Akbar"
b = "Harisma"
c = "Ramanda"
print (a, b, c)

#output variables pakai tambah
a = "Akbar "
b = "Yudha "
c = "Ramanda"
print(a + b + c)

#output variables mechanical
a = 10
b = 5
c = 6
print(a + b - c)

#global variable
#Create a variable outside of a function, and use it inside the function
x = "Awesome"

def myfunc():
    print("Python is " + x)

myfunc()

#Create a variable inside a function, with the same name as the global variable
x = "Awesome"
def myfunc():
    x = "Fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

#globalkeyword
def myfunc():
    global x
    x = "yada yada yada"
myfunc()
print("dia bilang " + x)

#use the global keyword if you want to change a global variable inside a function
x = "yada yada yada"
def myfunc():
    global x
    x = "ya ampun shay"
myfunc()
print("dia bilang " + x)
