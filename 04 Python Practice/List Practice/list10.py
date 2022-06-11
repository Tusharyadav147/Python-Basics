"""10. Write a Python program to find the list of words that are
longer than n from a given list of words."""

l = ["Tushar", "Meghanshu", "piyush", "Himanshu", "tarun"]
l1 = []
n = int(input("Enter the lenght: "))
for i in l:
    if len(i) > n:
        l1.append(i)
    else:
        pass

print(l1)