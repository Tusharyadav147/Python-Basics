"""Please write a program using generator to print the numbers which can be divisible by 5 and
7 between 0 and n in comma separated form while n is input by console."""

"""def NumGen(n):
    num = list(range(0,n+1))
    for i in num:
        if i % 5 == 0 and i % 7 == 0:
            yield i
        else:
            pass


if __name__ == "__main__":
    n = int(input("Enter the value of n here:"))
    print("The number which is divisible by 5 and 7 are:- ")
    for j in NumGen(n):
        print(j, end= " ")"""

"""Please write a program using generator to print the even numbers between 0 and n in comma
separated form while n is input by console."""

"""def EvenNumGen(n):
    num = list(range(0,n+1))
    for i in num:
        if i%2 == 0:
            yield i
        else:
            pass

if __name__=="__main__":
    n = int(input("Enter The Value Of N Here:"))
    print("The Even Num Between 0 and {}".format(n))
    for j in EvenNumGen(n):
        print(j, end=",")"""

"""Please write a program using list comprehension to print the Fibonacci Sequence in comma
separated form with a given n input by console."""

"""def FibSeq(n):
    num = list(range(n+2))
    n1, n2 = 0, 1
    for i in num:
        if i <= 1:
            yield i
        elif i > 1 and i < len(num):
            nth = n1 + n2
            n1 = n2
            n2 = nth
            yield n2
if __name__== "__main__":
    n = int(input("Enter how long seq you want:"))
    print("The Require Fib. Sequence Is:")

    for j in FibSeq(n):
        print(j, end=",")"""

"""Assuming that we have some email addresses in the &quot;username@companyname.com&quot; format,
please write program to print the user name of a given email address. Both user names and
company names are composed of letters only."""

"""import re

def check_email(email_address):
    check = "(\w+)@((\w+\.)+(com))"
    if re.match(check, email_address):
        return "Your Name Is {}".format(re.match(check, email_address).group(1))
    else:
        return "Enter A Vailed Email Address"

if __name__ == "__main__":
    email_address = input("Enter your email address here:")
    print(check_email(email_address))"""

"""Define a class named Shape and its subclass Square. The Square class has an init function
which takes a length as argument. Both classes have a area function which can print the area
of the shape where Shape&#39;s area is 0 by default."""

"""class shape():
    def __init__(self, area):
        self.area = 0
    def area(self):
        print(self.area())

class square():"""
