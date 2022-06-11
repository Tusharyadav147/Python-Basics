#functions 
"""def indore():              #definition of function
    print("Hello indore")
    print("Bye")

indore()   """        #calling of functions

from ast import operator


def car(x):
    print("Hello", x)

"""car("User")
#car()       #this will show error thtat missing 1 positional argument

a = input("Enter Your name: ")
car(a)"""

def talk(x,y):
    print(x+y)

talk(10, 20)
#talk(100)

#return statement 
"""def add(x,y):
    z = x+y
    return z

print(add(5,7))
b = add(8,9)
print(b)
print(type(b))"""

"""def greater(x,y):
    if x>= y:
        return x
    else:
        return y

i = int(input("Enter Number 1: "))
j = int(input("Enter Number 2: "))

result = greater(i, j)
print(result)"""

"""def said(msg, time= 1):
    return (msg*time)
print(said("Hello"))
print(said("Hi", 5))"""

"""def say(a, b = 5, c = 10):
    print(a)
    print(b)
    print(c)

say(15)
say(11,c =15)
say(12,13,14)
say(c= 55, a = 20)
"""

"""i = 0       #globel variable 
def change(i):
    i += 1    #it is a local varibale
    return 1

change(i)
print(i)
"""

#reference Function
def multiply(x,y):
    return x*y

operator = multiply
print(operator(7,3))