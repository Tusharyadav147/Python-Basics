#2. write a python program to multiplies all the item in list
l = [1,3,5,67,7,5,4]
n = 0
m = 1
while n< len(l):
    m *= l[n]
    n += 1
print(m)
