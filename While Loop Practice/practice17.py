"""17. Write a Python program to print alphabet pattern 'A'.
Expected Output:
 ***
*   *
*   *
*****
*   *
*   *
*   *
"""

center = int(input("Enter the length of A: "))
n = 0
while n<= 6:
    if n == 0:
        print(" ", end="")
        print("*"*(center-2))
    elif n < 3:
        print("*", end="")
        print(" "*(center-2), end="")
        print("*")
    elif n == 3:
        print("*"*center)
    elif n>= 4:
        print("*", end="")
        print(" "*(center-2), end = "")
        print("*")
    n += 1