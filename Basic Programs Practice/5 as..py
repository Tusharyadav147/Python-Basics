#Find LCM

"""print("Welcome To LCM Calculator i.e. You Can Calculate LCM Of Two Number")
num = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
num_1 = num
num_2 = num2
LCM = 1
print(num_1)
print(num_2)
print(" ",'|',num_1,",",num_2)
for i in range(2,100000):
    if num_1 > 1 or num_2 > 1:
        while num_1%i == 0 or num_2%i == 0:
            if num_1%i == 0:
               num_1 = num_1/i
            if num_2%i == 0:
               num_2 = num_2/i
            print(i,"|",num_1,",",num_2)
            print("-------------")
            LCM = LCM*i
print("The LCM Of",num,"and",num2,"is",LCM)"""

#Find HCM

"""print("Welcome To HCF Calculator i.e. Calculate HCF Of Two Numbers")
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
num_1 = num1
num_2 = num2
print(num_1,",",num_2)
HCF1 = 1
HCF2 = 1
Final = 1
for i in range(2,20):
    if num_1 >1 or num_2 >1:
        while num_1%i == 0 or num_2%i ==0:
            if num_1%i == 0:
                num_1 = num_1/i
                HCF1 = i
            elif num_2%i == 0:
                num_2 = num_2/i
                HCF2 = i
            if HCF1 == HCF2:
                Final = Final*HCF1
print("The HCF Of",num1,"and",num2,"is",Final)"""

#Decimal To Binary,Octal,Hexadecimal

"""num = int(input("Enter Any Number:"))
conversion_type = input('Enter Conversion Type i.e. Binary,Octal or Hexadecimal =')
num_1 = num
place = 1
print(num_1)
while num_1 > 0:
    if conversion_type == "Binary" and num_1 < 16:
        quotient = int(num_1/2)
        remainder = num_1%2
    elif conversion_type == "Octal":
        quotient = int(num_1/8)
        remainder = num_1%8
    elif conversion_type == "Hexadecimal":
        quotient = int(num_1 / 16)
        remainder = num_1 % 16
        if remainder > 10:
            if remainder == 10:
                remainder = "A"
            elif remainder == 11:
                remainder = "B"
            elif remainder == 12:
                remainder = "C"
            elif remainder == 13:
                remainder = "D"
            elif remainder == 14:
                remainder = 'E'
            elif remainder == 15:
                remainder = "F"
    print(place, "=", remainder)
    num_1 = quotient
    place = place + place"""

#Short Keys For Conversion of Decimal To Binary,Octal,Hexadecimal
"""dec = 344

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")"""
