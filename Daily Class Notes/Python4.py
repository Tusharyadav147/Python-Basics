#List functions
"""l = [10,20,4,5,63,7]
print(len(l))

print(max(l))
print(min(l))
print(sum(l))

l = [1,2,3,4,"A"]
print(sum(l))

l = ["A", "B"]
print(sum(l)) """  #this show int and str error which is because befault 0 is add firtly

#list methods
"""class list{ 
    inert()
    append()
}"""

"""n= [1,2,3]
print(type(n))

n.append(5)
n.insert(1,"beer")
print(n.index(2))
print(n.count(3))"""

"""print(ord("A"))
print(chr(35))

help(list)"""



#WAP to enter 5 element from user and append them into a list and print the list

"""l = []
n = 0
while n < 5:
    value = int(input("Enter value: "))
    l.append(value)
    n += 1
print(l)

n = 0
while n<5:
    print(l[n])
    n+=1"""

#WAP to enter 5 elements from user and print total and average of them
"""l = []
n = 0
while n < 5:
    value = int(input("Enter value: "))
    l.append(value)
    n += 1
print(l)

print("Total : ", sum(l))
print("Average: ",(sum(l)/len(l)))"""

#WAP to enter 5 elements from user and print sum of them without using sum function
l = []
n = 0
while n < 5:
    value = int(input("Enter value: "))
    l.append(value)
    n += 1
print(l)

n = 0
m = 0
while n<5:
    m += l[n]
    n+=1
print("Total : ", m)
print("Average: ",m/5)