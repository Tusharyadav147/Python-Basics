"""3. Make a list of each Boolean operator(i.e. every possible combination of Boolean
values for the operator and what it evaluate )."""

"""my_list = [True, False]
print(my_list)

#4. What are the values of the following expressions?

print((5 > 4) and (3 == 5))
print(not (5 > 4))
print((5 > 4) or (3 == 5))
print(not ((5 > 4) or (3 == 5)))
print((True and True) and (True == False))
print((not False) or (not True))

#5. What are the six comparison operators?

# >,<,>=,<=,==,\=

#7. Identify the three blocks in this code:

spam = 0
if spam == 10:
  print("eggs")
if spam > 5:
  print('bacon')
else:
  print('ham')
  print('spam')
  print('spam')"""

"""8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam."""

"""name = input('First Enter Your Name : ')
spam = int(input('Enter Your Number Here: '))

if spam == 1:
    print ("Hello" ,name)
elif spam == 2:
    print ('Howdy' ,name)
else:
    print ("Greetings!")"""

"""12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop."""

"""a = range(11)
for n in a:
  print(n)
n = 0
while n in range(0,11):
    print(n)
    n = n+1"""

#Convert Kilometer Into Meter

"""a = int(input("Enter Kilometer to Convert in meter: "))
print(a,'Kilometer')
b = a*1000
print(b,"meter")"""

"""import calendar
yy = 2021
mm = 4
print(calendar.month(yy,mm))"""

#To Solve Quadratic Equation ax**2+bx+c
"""import math
a = int(input("Enter The Coefficient of x**2:"))
print('a=',a)
b = int(input("Enter The Coefficient of x:"))
print('b=',b)
c = int(input("Enter The Constant Value:"))
print('c=',c)
value = (b)**2 - 4*a*c
c_1 = -(b) + math.sqrt(value)
c = c_1/2
print('The First Root of Equation Is=',c)

c_2 = -(b) - math.sqrt(value)
c = c_2/2
print('The Second Root Of Equation Is=',c)"""

#swap without third variable
a = 5
b = 8
a,b = b,a
print(a)
print(b)