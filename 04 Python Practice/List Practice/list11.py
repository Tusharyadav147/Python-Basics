"""11. Write a Python function that takes two lists and returns
True if they have at least one common member."""

l = ["Tushar", "Meghanshu", "piyush", "Himanshu", "tarun"]
l1 = ["chhout", "Pushpen", "harman", "soniya"]
m = 0
for i in l:
    if i in l1:
        m +=1
    else:
        pass
if m > 0:
    print(True)
else:
    print(False)