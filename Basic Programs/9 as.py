#Write a Python program to check if the given number is a Disarium Number?

"""def disarium(n):
    x = int(n)
    num = len(n)
    sum = 0
    l1 = []
    for i in range(1, num + 1):
        l1.append(i)
    l2 = []
    for j in n:
        l2.append(int(j))
    l3 = []
    for k in range(num):
        l3.append(int(l2[k]) ** l1[k])
        sum = sum + (int(l2[k])**l1[k])
    if sum == x:
        return 1
    else:
        return 0
n = input("Enter Any Number")
if disarium(n) == 1:
    print ("Your Number Is Disarium Number")
else:
    print("The Given Number Is Not Disarium Number")"""

#Write a Python program to print all disarium numbers between 1 to 100?

"""for m in range(1,101):
    n = str(m)
    num = len(n)
    sum = 0
    l1 = []
    for i in range(1, num + 1):
        l1.append(i)
    l2 = []
    for j in n:
        l2.append(int(j))
    l3 = []
    for k in range(num):
        l3.append(int(l2[k]) ** l1[k])
        sum = sum + l3[k]
    if sum == m:
        print(sum)
    else:
        pass"""

#Write a Python program to check if the given number is Happy Number?

"""def isHappyNumber(num):
    rem = sum = 0;

    # Calculates the sum of squares of digits
    while (num > 0):
        rem = num % 10;
        print(rem)
        sum = sum + (rem * rem);
        print(sum)
        num = num // 10;
        print(num)
    return sum;


num = 82;
result = num;

while (result != 1 and result != 4):
    result = isHappyNumber(result);

# Happy number always ends with 1
if (result == 1):
    print(str(num) + " is a happy number");
# Unhappy number ends in a cycle of repeating numbers which contain 4
elif (result == 4):
    print(str(num) + " is not a happy number");"""