#to reverse a number
"""n = int(input())
s = 0
while n > 0:
    r = n%10
    s = s*10 + r
    n = n//10
print(s)
    """


"""n = int(input())
s = 0
t = n
while n > 0:
    r = n%10
    s = s*10 + r
    n = n//10
print(s)

if s == n:
    print("It is palendrom number")
else:
    print("Not")"""

#chech
"""n = int(input())
while n > 0:
    r = n%10
    s = s*10 + r
    n = n//10
    print("Hello")
while s> 0:
    r = s%10
    print(r)
    s = s//10"""

#print number in character
"""d = {1 : "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 0: "Zero"}
n = int(input("Enter: "))
s = 0
t = n
while n > 0:
    r = n%10
    s = s*10 + r
    n = n//10
while s> 0:
    r = s%10
    print(d[r])
    s = s//10"""

#print Fractorial
"""num = int(input("Enter Any Number:"))
factorial = 1
if num < 0:
    print("Sorry The Factorial Of -ve Number Is Not Possible")
elif num == 0:
    print("The Factorial Of Zero Is 1")
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("The Factorial Of",num,"Is",factorial)"""

#the Fibonacci sequence?

"""num_1 = 0
print(num_1)
num_2 = 1
print(num_2)
for i in range(0,20):
    num_3 = num_1 + num_2
    print(num_3)
    num_1, num_2 = num_2, num_3
    print("passs")"""

"""n = int(input("Enter"))
m = 0
a = 0
b = 1
print(a)
print(b)
while m < n-2:
    c = a+b
    print(c)
    a, b = b, c
    m += 1"""

"""n = 1
m = 0
while n < 1001:
    if n%3 == 0 or n%5 == 0:
        if n%3 == 0 and n%5 == 0:
            pass
        else:
            m = m+ n
    n +=1

print(m)"""

print(32%10)