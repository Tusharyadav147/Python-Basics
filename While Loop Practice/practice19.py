"""19. Write a Python program to print alphabet pattern 'E'.
Expected Output:
*****
*
*
****
*
*
*****
"""
n = 6
i = 0
while i <= n:
    if i == 0:
        print("*"*n,end="")
        print()
    elif i <= 2:
        print("*")
    elif i == 3:
        print("*"*(n-1),end="")
        print()
    elif i <= 5:
        print("*")
    elif i == 6:
        print("*"*n,end="")
        print()
    i += 1