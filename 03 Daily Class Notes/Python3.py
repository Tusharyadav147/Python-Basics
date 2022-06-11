#nested while loop
"""i = 1

while i<= 3:
    j = 1
    while j<= 3:
        print(i,j, end="\t")
        j += 1
    print()
    i +=1
"""

"""i = 1
while i <=5:
    print("*"*i)
    i += 1"""

"""i = 1
while i<= 5:
    j = 1
    while j<= i:
        print("*", end="")
        j += 1
    print()
    i+=1
    """
"""
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1"""

"""i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(i, end=" ")
        j += 1
    print()
    i += 1"""

"""i = 5
while i >=1:
    j = 1
    while j <=i:
        print(j, end=" ")
        j += 1
    print()
    i -= 1"""

"""i = 5
while i >=1:
    j = 1
    while j <=i:
        print(i, end=" ")
        j += 1
    print()
    i -= 1"""

"""i = 5
while i >=1:
    j = 1
    while j <=i:
        print(5-(i-1), end=" ")
        j += 1
    print()
    i -= 1"""

"""i = 5
while i >=1:
    j = 0
    while j <i:
        print(i-j, end=" ")
        j += 1
    print()
    i -= 1"""


#list it is a different type of elements 
"""list = [10,10,5,"A",4]
print(type(list))

print(list[0])
print(type(list[0]))

list[1] = 100
print(list)

print(list[::0])"""
"""
rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print(i," ", end="")
        k += 1
   
    k = 0
    print()"""

"""rows = 5

k = 0
count=0
count1=0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print("  ", end="")
        count+=1
    
    while k!=((2*i)-1):
        if count<=rows-1:
            print(i+k, end=" ")
            count+=1
        else:
            count1+=1
            print(i+k-(2*count1), end=" ")
        k += 1
    
    count1 = count = k = 0
    print()"""