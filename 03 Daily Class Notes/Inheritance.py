"""class football:
    def goal(self,a,b):
        self.x = a
        self.y = b
    def show(self):
        print(self.x)
        print(self.y)
f1 = football()
f2 = football()

f1.goal(10,20)
f2.goal(7,5)

f1.show()
f2.show()

print(f1.x)"""

#contructor
"""is a special member method of the class
"""

"""class test:
    def __init__(self):           #magic methods, dundors
        print("Hello from contructor")

t = test()
"""
#parametric contructior

"""class test:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x)
        print(self.y)

t = test(5,8)
t.show()"""

#single level Inheritance
"""class A:     #parent class or super class or base class
    def add(self):
        print("Add A")

class B(A):     #child class or sub class or derived class
    def show(self):
        print("Show B")

a = A()
b = B()

a.add()
b.add()"""

#multi level inheritance
"""class A:     #parent class or super class or base class
    def add(self):
        print("Add A")

class B(A):     #child class or sub class or derived class
    def show(self):
        print("Show B")
class C(B):
    def display(self):
        print("Display")
a = A()
b = B()
c = C()

a.add()
b.add()
c.add()"""

#herirtical inheritance

"""class A:     #parent class or super class or base class
    def add(self):
        print("Add A")

class B(A):     #child class or sub class or derived class
    def show(self):
        print("Show B")
class C(A_CHARTEXT):
    def display(self):
        print("Display")
a = A()
b = B()
c = C()

a.add()
b.add()
c.add()"""

