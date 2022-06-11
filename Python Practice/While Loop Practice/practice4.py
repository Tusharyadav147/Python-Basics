"""4. Write a Python program to construct the following pattern,
using a nested for loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*"""

n = int(input("Enter how many star you want in center: "))
m = 2
for i in range(0, 2*n):
    if i <= n:
        print("*"*i)
    else:
        print("*"*(i-m))
        m += 2
