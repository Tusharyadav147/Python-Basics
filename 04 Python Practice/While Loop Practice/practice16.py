"""16. Write a Python program to find numbers between 100 and
400 (both included) where each digit of a number is an even
number. The numbers obtained should be printed in a
comma-separated sequence.
"""

n = 100
while n<= 400:
    if n%2 == 0:
        print(n, end=", ")
    n += 1