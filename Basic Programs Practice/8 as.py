#Write a Python Program to Add Two Matrices?

"""x = [[1,5,6],
     [6,9,8],
     [8,5,9]
    ]

y = [[5,6,9],
     [9,8,6],
     [3,6,4]
    ]
r = [[0,0,0],
     [0,0,0],
     [0,0,0],
    ]
for i in range(len(x)):
    for j in range(len(x[0])):
        r[i][j]= y[i][j]+x[i][j]
print(r)"""

#Write a Python Program to Multiply Two Matrices?
"""x = [[1,5,6],
     [6,9,8],
     [8,5,9]
    ]

y = [[5,6,9],
     [9,8,6],
     [3,6,4]
    ]
r = [[0,0,0],
     [0,0,0],
     [0,0,0],
    ]
for i in range(len(x)):

    for j in range(len(x[0])):
        r[i][0] = r[i][0] + x[i][j]*y[j][0]
        r[i][1] = r[i][1] + x[i][j]*y[j][1]
        r[i][2] = r[i][2] + x[i][j] * y[j][2]
print(r)"""

#Write a Python Program to Transpose a Matrix?
"""x = [[1,5,6],
     [6,9,8],
     [8,5,9]
    ]
r = [[0,0,0],
     [0,0,0],
     [0,0,0],
    ]
for i in range(len(x)):
    for j in range(len(x[0])):
        r[i][j] = x[j][i]
print(r)"""

#4. Write a Python Program to Sort Words in Alphabetic Order?
"""my_str = input("Write a sentence here:")
j = []
for i in my_str.split():
    j.append(i.lower())
j.sort()

for k in j:
    print(k)"""

#5. Write a Python Program to Remove Punctuation From a String?
"""str = input("write a word:")
j = ""
for i in str:
    if i.isalnum():
        j = j+i
    else:
        pass
print(j)"""