"""6. Write a Python program to count the number of even and odd
numbers from a series of numbers.
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_no = 0
odd_no = 0
for i in numbers:
    if i%2 == 0:
        even_no += 1
    else:
        odd_no += 1
print("Number of even numbers : ", even_no)
print("Number of odd numbers : ", odd_no)
