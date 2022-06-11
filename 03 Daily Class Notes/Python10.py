#exception Handling
"""Run time errors are called exceptions
"""

#ZeroDivisionError:
"""a = 1
b = 0
print(a/b)"""

try:
    a = 1
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("Not Divisible")