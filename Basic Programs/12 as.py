#Write a Python program to Extract Unique values dictionary values?

"""def test_dict(dict):
    s = {0}
    for i in dict.values():
        for j in i:
            s.add(j)
    return (s)

dict = {'gfg': [5, 6, 7, 8],
        'is': [10, 11, 7, 5],
        'best': [6, 12, 10, 8],
        'for': [1, 2, 5]}
print(test_dict(dict))"""
#Write a Python program to find the sum of all items in a dictionary?

"""def item_sum(dict):
    sum = 0
    for i in dict.values():
        sum = sum + i
    return sum

dict = {'a': 100, 'b':200, 'c':300}
print(item_sum(dict))"""

#Write a Python program to Merging two Dictionaries?

"""dict1= {'a': 100, 'b':200, 'c':300}
dict2= {'gfg': [5, 6, 7, 8],
        'is': [10, 11, 7, 5],
        'best': [6, 12, 10, 8],
        'for': [1, 2, 5]}

for i in dict2:
    dict1[i] = dict2[i]
print(dict1)"""

#Write a Python program to convert key-values list to flat dictionary?

"""test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March'],
             "tushar": 54631}
key = test_dict["name"]
value = test_dict["month"]
test_dict1 = {}
print(key, value)
for i in range(len(key)):
    test_dict1[key[i]] = value[i]
print(test_dict1)"""

#Write a Python program to insertion at the beginning in OrderedDict?
"""from collections import OrderedDict

inordereddict = OrderedDict([("Tushar", 1), ("Tarun",2)])
inordereddict.update({'manoj':1})
inordereddict.move_to_end("manoj", False)
print(inordereddict)"""

#Write a Python program to check order of character in string using OrderedDict()?

"""from collections import OrderedDict

def check_order(input, pattern):
    dict = OrderedDict.fromkeys(input)
    counter = 0
    for key,value in dict.items():
        if key == pattern[counter]:
            counter =counter + 1
            if counter == len(pattern):
                return True
    return False

input = 'engineers rock'
pattern = 'erg'

print(check_order(input, pattern))"""

#Write a Python program to sort Python Dictionaries by Key or Value?

"""dict = {"Tushar":'c', "Tarun": 'e', "Indrajeet": 'a', "Jay": 'd', "Sourabh":'b'}
dict1 = {}
l = []
for key, value in dict.items():
    l.append(value)
l.sort()
for values in l:
    for key, value in dict.items():
        if values == value:
            dict1[key] = value
        else:
            pass
print(dict1)"""