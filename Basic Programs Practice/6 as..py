#to Display Fibonacci Sequence Using Recursion

"""def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n-2)+fibo(n-1))

terms = int(input('Enter The Number Or Terms You Want='))

if terms > 0:
    print("Fibonacci Sequence")
    for i in range(terms):
        print(fibo(i))"""

#Find Factorial of Number Using Recursion

"""def fact(n):
    if n == 1:
        return n 
    else:
        return n*fact(n-1)         #function fact(n-1) means factorial of (n-1) i.e. (n-1)!
    
num = int(input("Enter Num. To Find Fractorial ="))
if num > 0:
    print("Factorial Of {}".format(num))
    print(fact(num))
else:
    print("Enter A Positive Number")"""

#cube sum of first n natural numbers
"""def cube(n):
    sumcube = 0
    for i in range(n+1):
        sumcube= sumcube + i**3
    return sumcube
num = int(input("Enter The nth Number ="))

if num > 0:
    print("The Cube Sum Of First", num ,"Natural Number")
    print(cube(num))
else:
    print("Please Enter A +ve Integer")"""

#calculate the natural logarithm of any number

"""import math

num = int(input("Enter No. To find Log Value ="))
b = int(input("Enter The Base Value ="))
print(math.log(num,b))"""

#Write a Python Program to calculate your Body Mass Index

height = float(input("Input your height in Feet: "))
weight = float(input("Input your weight in Kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))