#7. Write a Python program to remove duplicates from a list.

l = [1,1,4,2,3,4,4,45,5]

for i in range(len(l)):
    for j in range(i+1,len(l)-1):
        if l[i] == l[j]:
            l.remove(l[j])
        else:
            pass
print(l)