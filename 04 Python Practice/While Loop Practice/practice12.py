"""12. Write a Python program that accepts a sequence of lines
(blank line to terminate) as input and prints the lines as
output (all characters in lower case)."""

lines = input("Enter the string: ")
for i in lines.split(" "):
    print(i.lower())