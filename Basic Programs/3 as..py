#Check Num. Is +ve or -ve or zero
"""a = int(input("Enter Any Number:"))
print('You Enter The Number',a)
if a>0:
    print('Your Number Is +ve')
elif a<0:
    print('Your Number Is -ve')
else:
    print('Your Number Is Zero')"""

#Check Odd & Even Number

"""a = int(input("Enter Any Number:"))
print('You Enter The Number',a)

if a%2 == 0:
    print('The Number Is Even Number')
else:
    print('The Number Is Odd Number')"""

#Check Leap Year

"""a = int(input('Enter Year:'))
print('Your Enter Year',a)

if a%4==0:
    print('This Year Is Leap Year')
else:
    print('This Year Is Not A Leap Year')"""

#Check Prime Number

"""num = int(input('Enter Any Number:'))
print('You Enter',num)

flag = False
if num > 1:
    for i in range(2,num):
        if num % i ==0:
            flag = True
            break
if flag:
    print('The Number Is Not A Prime Number')
else:
    print('The Number Is Prime Number')"""
#TO Print All Prime Number

"""for num in range(0,10000):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)"""
