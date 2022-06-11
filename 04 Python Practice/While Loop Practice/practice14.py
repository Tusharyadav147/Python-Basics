"""14. Write a Python program that accepts a string and
calculate the number of digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2
"""

word = input("Enter Something: ")
letters = 0
digits = 0
a = 0
list = []
list[:] = word
while a< len(word):
    if list[a].isalpha():
        letters += 1
    elif list[a].isdigit():
        digits += 1
    a += 1
print("Total Numbers of Letters in {} is {}".format(word, letters))
print("Total Numbers of digit in {} is {}".format(word, digits))
