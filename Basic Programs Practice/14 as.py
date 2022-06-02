"""Define a class with a generator which can iterate the numbers, which are divisible by
7, between a given range 0 and n."""

"""def divcheck(n):
    for i in range(n):
        if i%7 == 0:
            value = True
            print(i, value)
        else:
            value = False

print(divcheck(20))"""

"""Write a program to compute the frequency of the words from the input. The output
should output after sorting the key alphanumerically."""

"""def check_freq(seq):
    dic_words = {}
    for word in seq.split():
        dic_words[word] = dic_words.get(word,0)+1
    word_sorted = list(dic_words.keys())
    word_sorted.sort()
    print(word_sorted)
    print("frequency chart:-")
    for i in word_sorted:
        print("{}:{}".format(i, dic_words[i]))
seq = input("Write word for which you want to check frequency:")
print(check_freq(seq))"""

"""Define a class Person and its two child classes: Male and Female. All classes have a
method &quot;getGender&quot; which can print &quot;Male&quot; for Male class and &quot;Female&quot; for Female
class."""

"""class Person(object):
    def __init__(self,gender):
        self.gender = gender
    def getGender(self):
        print(self.gender)

class male(Person):
    def __init__(self, gender):
        print("You are male so your gender is also :-")
        super().__init__(gender)

class female(Person):
    def __init__(self, gender):
        print("You are female so your gender is also :-")
        super().__init__(gender)

p1 = male("male").gender
p2 = female("female").gender
print(p1,p2)"""

"""Please write a program to generate all sentences where subject is in [&quot;I&quot;, &quot;You&quot;] and
verb is in [&quot;Play&quot;, &quot;Love&quot;] and the object is in [&quot;Hockey&quot;,&quot;Football&quot;]."""

"""subject = ["I", "You"]
verbs = ["Play", "Love"]
obj = ["Hockey", "Football"]

for sub in subject:
    for verb in verbs:
        for obje in obj:
            print(sub + ' ' + verb + " " + obje)"""

"""Please write a program to compress and decompress the string &quot;hello world!hello
world!hello world!hello world!&quot;."""

"""import zlib
s = 'hello world!hello world!hello world!hello world!'
# In Python 3 zlib.compress() accepts only DataType <bytes>
y = bytes(s, 'utf-8')
x = zlib.compress(y)
print(x)
print(zlib.decompress(x))"""

"""Please write a binary search function which searches an item in a sorted list. The
function should return the index of element to be searched in the list."""