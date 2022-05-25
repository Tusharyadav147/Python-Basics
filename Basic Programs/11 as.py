#Write a Python program to find words which are greater than given length k?

"""k = input("Enter The Length Of K:")
str = input("Write Your Sentence Here:")
str1 = ""
l = []
l.append(str.split())
print(l)
for i in range(len(l[0])):
    if len(l[0][i]) > 4:
        str1 = str1 + " " + l[0][i]
    else:
        pass
print(str1)"""

#Write a Python program for removing i-th character from a string?

"""i = int(input("Enter The Number Which Place You Want To Remove The Character:"))
str = input("Write Your Sentence Here:")
str = str.strip(str[i])
print(str)"""

#Write a Python program to split and join a string?

"""def split_string(string):
    list_string = string.split(" ")
    return list_string
def join_string(list_string):
    string = "-".join(list_string)
    return string

if __name__ =='__main__':
    string = "My Name Is Tushar"

    list_string = split_string(string)
    print(list_string)

    print(join_string(list_string))"""

#Write a Python to check if a given string is binary string or not?

"""def check_bin(string):
    p = set(string)
    s = {"0","1"}
    if s==p or p == {'0'} or p == {"1"}:
        return "This Given String Is Binary"
    else:
        return "Error:- The Given String Is Not Binary"

if __name__ == '__main__':
    string = "10101010100gcfxd"
    print(check_bin(string))"""

#Write a Python program to find uncommon words from two Strings?

"""def uncommon(str1, str2):
    dict = {}
    for a in str1.split():
        dict[a] = dict.get(a, 0) +1
    for b in str2.split():
        dict[b] = dict.get(b, 0) +1
    print(dict)
    word = ''
    for c in dict:
        if dict[c] == 1:
            word  =word + c + ','
        else:
            pass
    return word
if __name__ == "__main__":
    str1 = "My Name Is Tushar Sonp"
    str2 = "My Name Is Tarun Choudhary"
    print(uncommon(str1, str2))"""

#Write a Python to find all duplicate characters in string?

"""def duplicate(str):
    dict = {}
    word = ""
    for i in str:
        dict[i] = dict.get(i, 0) + 1
    for j in dict:
        if dict[j] > 1:
            word = word + j + ", "
    return word

print(duplicate("Helloo"))"""

#Write a Python Program to check if a string contains any special character?

"""def special_character(str):
    if str.isalpha() == True:
        return  "The Given String Is not contain a special character"
    else:
        word = ""
        for i in str:
            if i.isalpha() == True:
                pass
            else:
                word = word + i +','
        return "{} This are the special character in the given string".format(word)


print(special_character("Tushar"))"""
