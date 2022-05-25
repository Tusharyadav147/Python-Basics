"""18. Write a Python program to print alphabet pattern 'D'.
Expected Output:
*****
*    *
*    *
*    *
*    *
*    *
*****
"""
n = 10
i = 0
while i <= n:
    if i==0:
        print("*"*n, end= "")
        print()
    elif i <= 5:
        print("*", " "*(n-2),"*")
    elif i> 5 and i<7:
        print("*"*n, end= "")
    i +=1