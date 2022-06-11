"""5. Write a Python program to count the number of strings
where the string length is 2 or more and the first and last
character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""

l = ['abc', 'xyz', 'aba', '1221']
n = 0
m = 0
while n < len(l):
    q = l[n]
    if type(q) == str:
        if q[0] == q[-1]:
            m +=1
    else:
        pass
    n += 1
print(m)
