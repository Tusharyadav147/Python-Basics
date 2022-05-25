#Write a Python program to find sum of elements in list?

"""l = [5,6,3,8,9,1,5,5,0,5,0,55,5,5,22,1,4,]
sum = 0
for i in l:
    sum = sum + i
print(sum)"""

#Write a Python program to Multiply all numbers in the list?

"""l = [5,6,3,8,9,1,5,5,5596852,5,25,55,5,5,22,1,4,]
mult = 1
for i in l:
    mult = mult* i
print(mult)"""

#Write a Python program to find smallest number in a list?

"""l = [5,6,3,8,9,1,5,5,5596852,5,25,55,5,5,22,1,4,]
l.sort()
print("The Smallest Element In the list is:", l[0])"""

#Write a Python program to find largest number in a list?

"""l = [5,6,3,8,9,1,5,5,5596852,5,25,55,5,5,22,1,4,]
a = len(l)
l.sort()
print("The largest Element In the list is:", l[a-1])"""

#Write a Python program to find second largest number in a list?

"""l = [5,6,3,8,9,1,5,5,5596852,5,25,55,5,5,22,1,4,]
a = len(l)
l.sort()
print("The Second largest Element In the list is:", l[a-2])"""

#Write a Python program to find N largest elements from a list?

"""l = [5,6,3,8,9,1,5,5,5596852,5,25,55,5,5,22,1,4,]
N = int(input("Enter the value of N:"))
a = len(l)
l.sort()
for i in range(1,N+1):
    print("The {} largest Element In the list is:".format(i), l[a-i])"""

#Write a Python program to print even numbers in a list?

"""l = [5,6,3,8,9,1,5,5,5596852,5,25,55,5,5,22,1,4,]
for i in l:
    if i%2 == 0:
        print (i)
    else:
        pass"""

#Write a Python program to print odd numbers in a List?

"""l = [5,6,3,8,9,1,5,5,5596852,5,25,55,5,5,22,1,4,]
for i in l:
    if i%2 == 0:
        pass
    else:
        print(i)"""

#Write a Python program to Remove empty List from List?

"""l = [4.66,6,5,["Tushar",48,60], [], "Tusshar", [], 96]

for i in l:
    if type(i) == list:
        if len(i) == 0:
            l.remove(i)
        else:
            pass
    else:
        pass
print(l)"""

#Write a Python program to Cloning or Copying a list?

"""l = [4.66,6,5,["Tushar",48,60], [], "Tusshar", [], 96]
l1 = []
for i in l:
    l1.append(i)
print(l1)"""

#Write a Python program to Count occurrences of an element in a list?

"""l = [5,6,3,8,9,1,5,5,5596852,5,25,55,5,5,22,1,4,]
count_digit = int(input("Enter The Digit Which you want to count:"))
counter = 0
for i in l:
    if i ==count_digit:
        counter = counter + 1
    else:
        pass
print("This {} number is occurred in the list {} times".format(count_digit,counter))"""

