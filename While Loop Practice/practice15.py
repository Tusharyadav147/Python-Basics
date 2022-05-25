"""15. Write a Python program to check the validity of password
input by users.
Validation :
● At least 1 letter between [a-z] and 1 letter between [A-Z].
● At least 1 number between [0-9].
● At least 1 character from [$#@].
● Minimum length 6 characters.
● Maximum length 16 characters."""


password = input("Enter Your Password: ")
a = 0
list = []
list[:] = password
Special = ["$","#","@"]
alpha_count1 = 0
alpha_count2 = 0
digit_count = 0
special_count = 0
while a< len(password):
    if len(password) <6:
        print("You need atleast 6 characters in your password")
        break
    else:
        if list[a].islower():
            alpha_count1 += 1
        elif list[a].isdigit():
            digit_count += 1
        elif list[a].isupper():
            alpha_count2 += 1
        elif list[a] in Special:
            special_count += 1
        a += 1
if alpha_count1 != 0 and digit_count != 0 and special_count != 0:
    print("Your Password is Strong")
else:
    print("Your Password is weak \ncheck your password must contain following things:-\n● At least 1 letter between [a-z] and 1 letter between [A-Z].\n● At least 1 number between [0-9].\n● At least 1 character from [$#@].\n● Minimum length 6 characters.\n● Maximum length 16 characters.")
