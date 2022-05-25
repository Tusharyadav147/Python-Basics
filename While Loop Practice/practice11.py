"""11. Write a Python program which takes two digits m (row) and
n (column) as input and generates a two-dimensional array.
The element value in the i-th row and j-th column of the
array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1.
Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
"""

n = int(input("Enter number of rows: "))
m = int(input("Enter number of column: "))

array = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(i*j)
    array.append(row)
print(array)