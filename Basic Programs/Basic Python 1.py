#Modules and Exceptions
"""import math
print(math.sqrt(4))

from math import sqrt
print(sqrt(5))

from math import sqrt, pi
print(pi)

from math import *  # * means that we upload all the modules inside the math
print(sin(0))"""
"""import os
from gettext import install

import mysql
import pip
from mysql import connector
from pygments.lexers import pyt"""

"""import os
print(os.getcwd())
import Test

import Test  #We don't get any data bcz we import it once

import imp
imp.reload(Test)   #to reload the same data again"""

"""import Test1   #Create our own module
print(Test1.addition(4,9))
print(Test1.power(4,2))
print(Test1.multiplication(4,2))
"""

"""print(os.getcwd())
#os.mkdir("Test")
os.chdir(os.getcwd() + "/" + "test1")
print(os.getcwd())
#os.mkdir("Test")
os.chdir(os.getcwd() + "/" + "test")
print(os.getcwd())"""

"""f = open("mod1.py" , 'w')
m = open("mod2.py" , 'w')
n = open("mod3.py" , 'w')"""

#Exception Handling
"""try:   #a error is try to test as run time error and this error not catch syntatical error
    a = open("test.txt", "r")
except:
    pass

try:   #a error is try to test as run time error
    a = open("test.txt", "r")
except IOError as e:   #only work when error is input/ouput error
    print("There is a error",e)

try:   #a error is try to test as run time error
    a = 5/5
except ArithmeticError as e:
    print("There is a error",e)
else:
    print("This will execute once try will execute with sucess")"""

"""l = [1,5,6,8,3,6]
print(l[100])
t = (1,3,5,65,80)   # this part is not executed bcz there is some issue in before this code
print(t)"""

"""try:
    l = [1,2,5,6,3,4,5]
    print(l[100])
except:
    print("There is some issue in the code")
    t = (1, 3, 5, 65, 80)
    print(t)
    try:
        t[0]= "Tushar"
    except:
        pass
else:
    print("There is no issue with my code")"""

#work with finally
"""try:
    f = open("Test.txt", "w+")
except:
    pass
else:
    print("else will execute if try will execute with suc.")
finally:
    print("Finally i will execute in any case")
    l = [1, 2, 5, 6, 3, 4, 5]
    print(l[1])"""

"""def askforint():
    while True:    #this is an infinite loop
        try:
            a = int(input("Enter an integer"))
        except Exception as e:
            print("This is my error msg",e)
        else:
            print("Person has entered a correct value")
            break
        finally:
            print("Close this issue")
askforint()"""

#Create Our own exception
"""def create_your_exception(a):
    if a > 6:
        raise Exception("error is ",a)
    else:
        print("Input is ok")
    return a

try:
    create_your_exception(10)
except Exception as e:
    print(e)"""

#Daily Task
"""import os
print(os.getcwd())
os.mkdir("Test2")
os.chdir(os.getcwd() + '/' + "Test2")
print(os.getcwd())"""
#f = open("mod1.py", 'w+')

#object orianted programming OOPS languages
#class and object
"""class car:
    pass
audiq7 = car()
print(audiq7)

nano = car

nano.milage = 20
nano.year = 2020
nano.make = 2221
nano.model = "sjbhghha"
nano.engine = 220

print(nano.model, nano.make, nano.year)"""

#write same program in simple manner

"""class car:

    def __init__(self, milage , year, make, model):   #We can use anyword in place of self as a, b, fdds, anything that we want
        self.milage = milage
        self.year = year
        self.make = make
        self.model = model

    def age(self1,current_year):   #self, self1, self2,self3 is nothing but a pointer 
        return current_year - self1.year

    def milage1(self2):
        #print("The Milage of your car is", self.milage())
        return self2.milage

    def __str__(self3):
        return "This is my car class i have created"


nano = car(2654, 2002, 21, "dgtysg",)
print(nano.milage, nano.model, nano.make, nano.year)
print(nano.age(2021))
print(nano.milage1())
print(nano)"""

"""class student:

    def __init__(self, name, rollno, joining_date, current_topic):
        self.name = name
        self.rollno = rollno
        self.joining_date = joining_date
        self.current_topic = current_topic

    def crt_topic(self):
        print("This current topic dicussed in my class is", self.current_topic)

    def srt_rollno(self):
        try:
            if type(self.rollno) == str:
               print("Do nothing")
            else:
               return  str(self.rollno)
        except Exception as e:
            print("This is my error msg")

    def duration(self,current_date):
        print("Duration of student in my class is", current_date - self.joining_date)

    def __str__(self):
        return "This is student class where they can try to input there own data and they can try to fratch it"

tushar = student("Tushar", 495, 2021, "python")
tushar.duration(2021)

print(tushar)
print(tushar.current_topic)
print(tushar.crt_topic())
print(tushar.srt_rollno())"""

"""import logging as lg
lg.basicConfig(filename="Errorfile.log", level= lg.INFO, format= "%(asctime)s %(message)s %(levelname)s ")
class data:
    def __init__(self, filename , filetype, date, size):
        self.filename = filename
        self.filetype = filetype
        self.date = date
        self.size = size

    def file_open(self1):
        lg.info("The File Is opened")
        try:
            f = open(self1.filename + "." + self1.filetype , 'w+')
            f.write(input("Write Something In File: "))
            f.close()
            lg.info("Your msg is written in the file")
        except Exception as e:
            print(e)
            lg.error(e)

    def file_read(self2):
        lg.info("File data is reading")
        try:
            f = open(self2.filename + "." + self2.filetype , 'r')
            print(f.read())
            f.close()
        except Exception as e:
            print(e)
            lg.error(e)

    def file_append(self3):
        lg.info("Your Appending data into file")
        try:
            f = open(self3.filename + "." + self3.filetype, 'a')
            f.write(input("Append data into your file: "))
            f.close()
            self3.file_read()
        except Exception as e:
            print("There is an error as: ", e)
            lg.error(e)

personal = data("myfile", "py" , 2020, 10)
personal.file_open()
personal.file_read()
personal.file_append()"""

#Abstraction  is a symbolic things in python & inheritance & incaptulation
"""class test:
    def __init__(self, a, b, c, d):
        self.__a  = a     # no underscore (a) variable means public variable, single underscore _a variable means its protactive, double underscore __a variable means its private variable
        self.b = b
        self.c = c
        self.d = d

    def test_custome(self,v):
        return v - self.__a

    def __str__(self):
        return "This is my test code for abstraction"

o = test(1,5,6,7)
print( o.test_custome(7))
print(o)
#print(o.__a)      #this is what how abstraction of python will come into picture
print(o._test__a)    #private variable is calling as

class test1(test):  #here test1 is child class and test is parent class
    def __init__(self, j, *agrs):
        super(test1, self).__init__(*agrs)   #super mean its call the parent class thats test class
        self.j = j

m = test1(4,5,6,7,8)
print(m.b)
print(m.j)
print(m.test_custome(9))    #by class test  we can reutilise test_custome method
print(m.c)
print(m.d)"""


class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')


class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')


d1 = Dog()

"""class test():
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def __str__(self):
        return  "this is the return form my test class"

class test1():
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        return "this is the return form my test1 class"

class test2():
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def __str__(self):
        return  "this is the return form my test2 class"

class final:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z  = z
    def __str__(self):
        return str(self.x) + "\n" + str(self.y) + "\n" + str(self.z)

t = test(4,5,6,7)
t1 = test1(1,2,3,7)
t2 = test2(5,6,8,9)
f = final(t,t1,"Tushar")
print(f)"""

"""class tushar:
    address = "Gwaltoli"
    name = "Tushar Sonp"
    father_name = "Naresh kumar Sonp"

    def contact_number(self):
        print(8085545457)

class detail(tushar):
    def __init__(self):
        self.year_of_ago = 20

    def all_details(self):
        print("{} is the son of {} and he is {} year ago, his contact numner is {}, and they are from {}".format(self.name,self.father_name,self.year_of_ago,self.contact_number(),self.address))

t = detail()
t.all_details()
t.contact_number()"""

"""class parent:
    a = 10
    b = 20
    def __init__(self,parent_a, parent_b):
        self.parent_a = parent_a
        self.parent_b = parent_b

class child(parent):
    def __init__(self):
        print(parent.a)
c = child()

#example of iheritance
class parent:
    a = 10
    b = 20
    def __init__(self,parent_a, parent_b):
        self.parent_a = parent_a
        self.parent_b = parent_b

class child(parent):
    def __init__(self,*args):
        super(child,self).__init__(*args)

cc = child(255,689)
print(cc.parent_b)"""

"""class student:
    def __init__(self, name, student_id, school_name, address):
        self.name = name
        self.student_id = student_id
        self.school_name = school_name
        self.address = address
    def __str__(self):
        return  "Detail:"+ "\n" + "\t" + str(self.name) + "\n" + "\t" + str(self.school_name) + "\n" + "\t" + str(self.student_id) + "\n" + "\t" + str(self.address)

stud = student("Tushar", 1811402, "United alphaa", "Gwaltoli")
print(stud)

class dog:
    def __init__(self, name, year_of_birth, breed):
        self.name = name
        self.year_of_birth = year_of_birth
        self.breed = breed
    def __str__(self):
        return "%s is a %s born in %s." % (self.name, self.year_of_birth, self.breed)

jacky = dog("Jacky", 1954, "Laika")
print(jacky)

dog = student(jacky , 45 , "dog_schl" , "dbsj" )
print(dog)"""

"""class  multiplynumeric():
    def __init__(self,a):
        self.a = a
    def __mul__(self, other):
        return self.a - other.a   #we can you any operator

mul = multiplynumeric(10)
mul1 = multiplynumeric(2)

print(mul * mul1)"""

"""class ineuron:
    def msg(self):
        print("This is a msg to ineuron")

class xyz:
    def msg(self):
        print("This is the msg to xyz")

def test(notes):
    notes.msg()

i = ineuron()
x = xyz()

test(i)
test(x)"""
