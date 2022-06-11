#function as a argument
"""def sub(x,y):
    return x+y

def do(red,x,y):
    return red(red(x,y), red(x,y))

a = 5
b = 10

print(do(sub, a,b))"""

"""def square(x):
    return x*x

def test(blue,x):
    print(blue(x))

test(square,9)"""

"""def green(red,a):
    print(red(a))

green(max, [1,2,3,5])
green(min, [1,4,5,6,0])"""

"""def printn(x):
    for i in range(x):
        print(i)
        return
printn(10)"""


#lambda function & anonymous function
"""def cube(y):
    return y**3

goa = lambda x: x**3
print(cube(5))
print(goa(7))"""

#filter function
"""n = [11,22,33,44,55]
r = filter(lambda x: x%2 ==0, n)
for i in r:
    print(i)"""

"""n = [11,22,33,44,55]
r = list(filter(lambda x: x>20, n))
print(r)"""

#map function
"""def add(x):
    return x+5

n= [1,2,3,4,5]
r = list(map(add,n))
print(r)"""


#Tuple
t = (4,3,4,5,6)
print(t)
print(type(t))
print(t[3])

