"""Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated
sequence."""

"""import math

C = 50
H = 30

D = int(input("Enter The Value of D"))

Q = math.sqrt((2 * C * D)/H)
print(int(Q))"""

"""Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡Y-1."""

"""X = int(input("Enter First Number:"))
Y = int(input("Enter Second Number:"))
arr = []
counter = 0
for i in range(X):
    arr.append([])
    for j in range(Y):
        arr[i].append(i*j)
print(arr)"""

"""Write a program that accepts a comma separated sequence of words as input and prints the
words in a comma-separated sequence after sorting them alphabetically."""

"""word = input("Type a comma separated sequence here:")
words = []
for i in word.split(","):
    words.append(i)
s = set(words)
print(s)
print(",".join(sorted(s)))"""

"""Write a program that accepts a sequence of whitespace separated words as input and prints
the words after removing all duplicate words and sorting them alphanumerically."""

"""word = input("write a sequence of whitespace words:")
set_words = set(word.split(" "))
final = list(set_words)
final.sort()
print(final)"""

"""Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:"""

"""str = input("write a sentence here:")
counter_letters = 0
counter_digits = 0

for i in str:
    if i.isalpha():
        counter_letters = counter_letters + 1
    elif i.isdigit():
        counter_digits = counter_digits + 1
print("There are {} no. of letters and {} no. of digits in the sentence".format(counter_letters, counter_digits))"""

"""A website requires the users to input username and password to register. Write a program to
check the validity of password input by users."""

"""password = input("Enter here password to check which one is correct:")

special_char = "[@_!#$%^&*()<>?/\|}{~:]"
for i in password.split(","):
    up = 0
    lo = 0
    dig = 0
    spe = 0
    for j in i:
        if len(i)>6 and len(i)<12:
            if j.isupper():
                up = up + 1
            elif j.islower():
                lo = lo + 1
            elif j.isdigit():
                dig = dig + 1
            for k in special_char:
                if k in j:
                    spe = spe + 1
    if up>0 and lo>0 and dig>0 and spe>0:
        print("{} this password is fullfill all the requirement".format(i))"""
