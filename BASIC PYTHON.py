#print('This is the first program')
#this is a comment line
"""this
is 
the
multi
line 
comment"""

#variable Assignment

"""a = 154
print(a)
b = "tushar"

a,b,c = 124,"tushar",1.52

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c)) """

#Input Function

"""a = input("Enter Something :")
print(a)"""

#String
"""t = "Tushar"
print(t[3])
print(t[0:6:2])
print(t[::-1])
print(t.upper())
print(t.lower())
for i in range(0,len(t)):
    print("Tushar")"""

#Small Logic
"""n = 7
for i in range(0,n):
    for j in range(0,i+1):
        print("+",end=" ")
    print("\r")"""

"""n = 7
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()"""

"""n = 9
m = 0
i = 0
j = 0
while i in range(0,9):
    while j in range(0,n):
        print(' ',end = " ")
        j = j + 1
    j = 0
    while j in range(0,i+1+m):
        print("*",end= " ")
        j = j + 1
    print()
    m = m + 1
    j = 0
    n = n-1
    i = i + 1"""

#In Simple Form
"""n = 9
i = 0
while i < n:
    print(" "*(n-i-1) + "* "*(i+1))
    i += 1"""

#List Concept

"""l = [1,2,55,5,55,9,23,556,4,]
l1 = list()
l2 = []
print(type(l1))
print(type(l2))
l1 = ["dyusfij",3257415,["dhu",25,"dj"],4+9j]
l1.append(1)
l1.append("my ")
l1.insert(3,"Tushar")
l1.extend("Tushar")
l.sort()
list = [i for i in "Tushar"]
print(list)
print(l)
print(l1)"""
#for i in l1:
    #print(type(i))


#Use Of Some Inbuild Fuction

"""s =  'we all are a part of FULL stack'
print('All The Word Are In Lower Case as =',s.lower())
print('The No. Of a In The string s is =',s.count('a'))
print('New Replace String Is =',s.replace('a','ineuron'))
for i in range(len(s)):
    if s[i] == 'a':
        print('Index of a in s =',i)
print(s.split())
print("{} name {} Tushar".format('My','is'))"""

#Append 2 more list and one is complex number in this list in between a exixting list
"""list = [[1,"hfj",2.58],["gdu",25,"fdy"],[5,8,"tur"]]
list.insert(1,[25,654,"dhdgjh"])
list.insert(2,[256,59,'tytweu'])
list.append(2+3j)
print(list)"""

#if your nested list contain string then find out it index in nested list and print it the remove the string
"""list1 = [[1,"hfj",2.58],["gdu",25,"fdy"],[5,8,"tur"],54,84,"yri"]
for i in list1:
    if type(i) == list:
        for j in i:
            if type(j)== str:
                print("index of {} is =".format(j),i.index(j))
                i.remove(j)
                print(list1)
            else:
                pass
    elif type(i) == str:
        print("index of {} is =".format(i),list1.index(i))
        list1.remove(i)
    else:
        pass
print("The Final List WithOut Any String =",list1)"""

#You Have to extract 2nd element of nested list

"""list1 = [[1,"hfj",2.58],["gdu",25,"fdy"],[5,8,"tur"],54,84,"yri"]
for i in list1:
    if type(i) == list:
        for j in i:
            if i.index(j) == 1:
                print("The Extracted Element Is =",j)
                i.pop(1)
            else:
                pass
    else:
        pass
print(list1)"""

#Some simple way to write code

list = []
"""for i in range(10):
    if i%2 == 0:
        list.append(i)
print(list)

print([i for i in range(10) if i%2 == 0])  #list compariation

for i in range (10):
    if i%2 != 0:
        list.append("odd")
    else:
        list.append("even")
print(list)

#By List Compariation

print(["odd" if i%2!=0 else "even" for i in range(10)])"""

"""mat = []
for i in range(3):
    mat.append([])
    for j in range(3):
        mat[i].append(j)
print(mat)"""

#By List Compariation

#print([[j for j in range(3)]for i in range(3)])

#Truples, note truple are immutable
"""t = ()
print(type(t))
t = (1152,3254,125,1.25,True)
print(t[0:2])
print(t[2])
print(t[::-1])
print(max(t))
print(t.index(125))
print(t.count(1.25))"""

#Set there is not index operation in the set
"""s = set()
print(type(s))
l = [1,1,1,2,5,53,53,5,4,4,56,66,6,6,"Tushar","tushar","tushar"]
print(set(l))
s.add("Tushar")
s.add('dhdfushs')
s.add(26)
print(s)
s.remove(26)
print(s)
s.clear()
print(s)"""

#dict
x = {}
"""print(type(x))
x = {1,5,265,26,55,"TUdiysig"}
print(type(x))
x.update({"Tushar": 4874})
print(x)"""

#Take input as a paragraph by using input function
#Q1
"""a = input()
e = a.split(" ")
print(e)
#Q2
print(set(e))
#Q3
b = {}
for i in set(e):
    b.update({i: "Tushar"})
print(b)
#Q4
c = tuple(b.values())
print(c)
#Q5
d = [b.keys()]
print(d)"""

#Function In Python

#Difference Between print and return statment

"""def add(a,b):
    print(a+b) #it only print the output
add(1,2)

def add1(a,b):
    return(a+b) #it return the value to the def  function
print(add1(1,2)+25)

def test(x,y):
    return x*10 , y *40 , x+y, x*y
print(test(1,2))
a,b,c,d = test(1,2)
print(a)
print(b)
print(c)
print(d)

a,b,c,_=test(1,3) #here _ is a place holder
print(a)
print(b)
print(c)
print(_)

a,b,_,_=test(1,3) #here _ is a place holder
print(a)
print(b)
print(_)
print(_)

def test1():
    return "This is my first function"
m = test1() + "Tushar Sonp"
print(m)

def test2(n):
    return n * 2
print(test2([1,15, 4,65326,65]))

def test3(*args):
    l = []
    for i in args:
        #l.append(i)
        l = l +i
    return l
print(test3([1,2,55,66,85,99],[2,4,9,85,98,59,8]))   #This is only true for same concatination otherwise we have to change the program

def test3(**kwargs):  #kwargs allow only the key,value pair
    return kwargs
print(test3(a=8, b=9, c=6, d=5))"""

#Q1 Create a function to take any number of mixed data and try to create a list of seperate data base on datatype and retrun multiple result

"""def separator(*args):
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    for i in args:

        if type(i) == str:
            l1.append(i)

        elif type(i) == int:
            l2.append(i)

        if type(i) == float:
            l3.append(i)

        if type(i) == bool:
            l4.append(i)
    return l1,l2,l3,l4

print(separator("dwjdbwukhg",2154,"dkhs",15.25,True,225,False,25525.1545))"""

#Q2 Create a  function which will be able to use args and kwargs and it will able to do all the list value concatination and retrun a list

"""def fun2(*args,**kwargs):
    l = [i for i in args]
    d = [i for i in kwargs.items()]
    return l,d
print(fun2([1,656,56,5,6,5,],598659,652,6,5,6746,4, b = 5, a= "fdhdug") )"""

#lambda Function e.i. a function without a name

"""m = lambda x,y: x+y
print(m(5,5))
print(m("Tushar"," Sonp"))
n  = lambda arg1,arg2: print(arg1,arg2)
print(n("Tushar","Sonp"))"""

#Difference Between Iterator and Iterable

"""for i in "Tushar": #for function is iterable
    print(i)

l = [1,2,5,3,6,7]
l = iter(l)
print(next(l)) #next function is iterator
print(next(l))
print(next(l))
print(next(l))
print(next(l))"""

#Generator Function

"""def test(n):
    for i in range(n):
        yield i**3

test(30)

for i in test(30):
    print(i)"""

"""def gent(n):
    a = 1
    b = 1
    output = []
    for i in range(n):
        output.append(a)
        a , b = b , a+b
    return output
print(gent(5))"""

#using generation menthod

"""def gent1(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a , b = b , a+b

print(gent1(6))

for i in gent1(6):
    print(i)"""

#How To open and create a new file

"""f = open("Tushar.txt","w")    #use mode w for writing something into the file
f.write("Tushar Sonp This is the new file you create")
f.close()

f = open("Tushar.txt","r")   #use mode r for reading the file
print(f.read())
print(f.read())  #there is no print because the cursor is at the end or create word so there is no word to read more
f.seek(0)        #reset the cursor position on that position e.i. 1
print(f.read(11))
f.close()

f = open("Tushar.txt", 'a')  #use mode a for appending more words into the file
f.write(" here we start appending something onto the same file by using mode a")
f.close()

f = open("Tushar.txt",'r')
print(f.read())
f.close()"""

"""f = open("Tushar.txt", 'r')
print(f.read())
f.seek(0)
print(f.readline()) #read only one line in which cursor is currently available
print(f.readline())
print(f.readline())
print(f.readline())
f.close()"""

"""f = open("Tushar.txt",'r')

for i in f:
    print(i)
    
f.close()"""

#How to check our current running file is where
"""import os
print(os.getcwd())
print(os.listdir())"""
#os.mkdir("Tushar")  #Create New folder in current location or create a new dir.
#os.rmdir("Tushar")  #To Remove particular Folder

"""if "Tushar.txt" in os.listdir():
    print("This is available in the dir")
    f = open("Tushar.txt","r+") #Here r+ is for read and write both operation
    print(f.readline())
else:
    print("This file is not available in this dir")"""


#Q1 Create A new directory

"""import os

os.mkdir("Tushar")"""

#Q2 Create 10 tst file and write some data in all txt at a time

"""for i in range(0,3):
    f = open(input("Enter Your File Name :"),"w")
    f.write(input("Enter Some Information Into The file :"))
    f.close()"""

#Q3 Read all the data from this dir/file print in console

"""import os
print(os.getcwd())
os.chdir("C:\\Users\DELL\PycharmProjects\pythontuts\Tushar")
print(os.getcwd())
for i in os.listdir():
    print(i)
    f = open(i,"r+")
    print(f.read())
    f.close()"""

#Q4 Hold all the data into a list

"""import os
print(os.getcwd())
os.chdir("C:\\Users\DELL\PycharmProjects\pythontuts\Tushar")
print(os.getcwd())
l = []
for i in os.listdir():
    print(i)
    f = open(i,"r+")
    l.append(f.read())
    f.close()
print(l)"""

#Q5 Write all the data in a new file from list

"""f = open("Tushar4.txt", "w")
for i in l:
    f = open("Tushar4.txt", "a")
    f.write(i)
    f.close()
f = open("Tushar4.txt",'r')
print(f.read())
f.close()"""

#Q6 Keep only a new file in present dir. and move rest in new dir.

"""import os
print(os.getcwd())
os.chdir("C:\\Users\DELL\PycharmProjects\pythontuts\Tushar")
print(os.getcwd())

for i in os.listdir():
    if not "Tushar4.txt" :"""
        #INCOMPLETE

#logging as debugging

"""import os

os.mkdir("logging")
os.chdir(os.getcwd() + "/" + "logging")

import logging as lg

lg.basicConfig( filename = 'test.log', level= lg.INFO, format = '%(asctime)s %(message)s')
lg.info("i am going to start my program")
lg.warning("this is the first warning to modify this program")
lg.error("There is an error")

def test(a,b):

    try:
        div = a/b
        return div
    except Exception as e:
        print("There is an error you can check this into logging")
        lg.error("error has occured")
        lg.exception(str(e))
        
print(test(4,0))"""

"""import logging as lg

lg.basicConfig(filename="test.log", level=lg.INFO)

def test(a,b):
    lg.info("The program started")
    return a+b

print(test(1,5))
logging.shutdown()"""

# Q1. create a logger in yuor code
# Q2. create one function which can take any number of input as an argument and it will be able to return sum of it.
# Q3. capture user input in log
# Q4. give user instruction in log file
# Q5. read a log file from python code and show all the cansole.

"""import os
print(os.getcwd())
os.chdir(os.getcwd() + "/" + "Tushar")
print(os.getcwd())

import logging as lg

def addition(*args):
    lg.basicConfig(filename="myprogram.log" , level=lg.INFO)
    lg.info("The program is started")
    sum1 = 0
    for i in args:
        lg.info(str(i))
        sum1 = sum1 + i
    lg.info(str(sum1))
    return sum1
print(addition(1,25,6,63,5,9,0))

f = open("myprogram.log" , 'r')
print(f.read())"""


"""import logging as lg

lg.basicConfig(filename="test1.log" , level = lg.DEBUG , format= '%(asctime)s %(name)s %(levelname)s %(message)s',filemode='w')
console_log = lg.StreamHandler()
console_log.setLevel(lg.DEBUG)
format = lg.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
console_log.setFormatter(format)
lg.getLogger().addHandler(console_log)
lg.info("This is my first test code for log")
logger1 = lg.getLogger("user1")
logger2 = lg.getLogger("user2")
logger3 = lg.getLogger("user3")
logger4 = lg.getLogger("user4")
logger1.info("this info is for logger 1")
logger2.debug("this debug is for logger 2")
logger2.info("this info is for logger 2")
logger3.info("this info is for logger 3")"""

#how to implement debugger

"""import ipdb

def testdebug():
    ipdb.set_trace()
    l = []
    for i in range(10):
        for j in range(5):
            l.append(i)
            if i ==4:
                continue
            print("We have appended your data in list")
    return l
print(testdebug())"""

#@