"""1. Write a Python program to find those numbers which are
divisible by 7 and multiple of 5, between 1500 and 2700 (both
included)."""
n = 1500
while n >= 1500 and n <= 2700:
    if n % 7 == 0 and n % 5 == 0:
        print("{} divisible by 7 and multiple of 5".format(n))
    n += 1

