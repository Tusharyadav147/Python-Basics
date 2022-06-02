#Q1 find sum of array

"""list = [1,2,3,5,6,7.25,]
sum_list =  0
for i in list:
    sum_list = sum_list + i
print(sum_list)"""

"""def add_list(a):
    j = 0
    for i in a:
        j = j + i
    return j
print(add_list([1,33,656,5,4]))"""
#Q2 find largest element in an array

"""list = [25,16,36,45,20,10,65,22,21]     #list.append(input("Enter No. To Add In List = "))
num1 = list[0]
for i in list:
    if num1 > i:
        pass
    elif num1 < i:
        num1 = i
print(num1)"""

#Q3 array rotation

"""list = [1,3,4,9,6,5]
list1 = []
rotation_num = int(input("Enter rotation time e.i. 1 to 6times ="))
k = 0
if rotation_num >0:
    for j in range(0, rotation_num):
        list1.append(list[j])
    for i in range(0,6):
        if i+rotation_num < 6:
            list[i] = list[i+rotation_num]
        elif i+rotation_num > 5:
            list[i] = list1[k]
            k = k+1
    print("Rotated list Up to {}times =".format(rotation_num),list)"""

#Q4 Split the array and add the first part to the end

"""list = [1,3,4,9,6,5]
sum = 0
for i in list:
    sum = sum + i
print(sum)"""

#given array is Monotonic

"""def isMonotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
print(isMonotonic([5,4,3,2,1,1,1]))
"""


