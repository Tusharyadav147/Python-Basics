"""9. Write a Python program to get the Fibonacci series between
0 to 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers
before it.
Expected Output : 1 1 2 3 5 8 13 21 34"""

n = int(input("Enter lenght of series: "))
m = 0
a = 0
b = 1
print(a, end=", ")
print(b, end = ", ")
while m < n-2:
    c = a+b
    print(c, end = ", ")
    a, b = b, c
    m += 1