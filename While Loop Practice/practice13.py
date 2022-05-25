"""13. Write a Python program which accepts a sequence of comma
separated 4 digit binary numbers as its input and print the
numbers that are divisible by 5 in a comma separated
sequence.
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010"""

seq = input("Enter the sequence of comma separated 4digits binary number: ")
def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal
for i in seq.split(","):
    if binaryToDecimal(int(i))%5 == 0:
        print(i)
    