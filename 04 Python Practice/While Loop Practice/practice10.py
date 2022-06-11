"""10. Write a Python program which iterates the integers from 1
to 50. For multiples of three print "Fizz" instead of the
number and for the multiples of five print "Buzz". For
numbers which are multiples of both three and five print
"FizzBuzz".
"""
for i in range(1,50):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz", end=", ")
    elif i%3 == 0:
        print("Fizz", end=", ")
    elif i%5 == 0:
        print("Buzz", end=", ")
    else:
        print(i, end=", ")