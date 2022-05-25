"""2. Write a Python program to convert temperatures to and from
celsius, fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius
and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius"""

print("Select the conversion type(i.e. Select 1 or 2):- \n1) Convert Celsius into fahrenheit \n2) Convert fahrenheit into Celsius")
n = int(input("Enter 1 or 2: "))

if n == 1:
    c = int(input("Enter Temperature: "))
    f = (c*9/5) + 32
    print("{} Celsius in fahrenheit is = {}".format(c,f))

elif n == 2:
    f = int(input("Enter Temperature: "))
    c = (f-32)*5/9
    print("{} fahrenheit in celsius is = {}".format(f,c))

