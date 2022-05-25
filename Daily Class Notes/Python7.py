# #Dictionary
# d = {1:1,2:2,3:4,5:7}
# print(d[1])

# #dictionary function
# d = {1:1, 2:18, 3:9, 4:16}
# print(len(d))

# print(max(d))
# print(min(d))
# print(sum(d))

# #methods in dictionary
# d = {1:"Apple", "orange": [2,4,5], 5:"Indore"}
# print(d.get("orange"))
# print(d.get(53,"Element not found"))

# f = {1:1,2:1,3:2,4:3}
# print(f.get(4,0)+ f.get(7,5))

# #clear
# f.clear()
# print(f)

# #key
# print(f.keys())

# #values
# print(f.values())

# r = {"one": "A", 5: "Zara", "one": "Maza"}
# print(r)

# r.items()

# d = {"x":100, "y": 200, "z":300}
# for a,b in d.items():
#     print(a,"-->",b)

"""dic = {}
for i in range(1,11):
    dic[i] = i*i
print(dic)"""

#WAP to merge 2 dictionaries

dic1 = {1:3,4:5}
dic2 = {"name": "Tushar", "mob": 8085545}

for i in dic1:
    dic2[i] = dic1