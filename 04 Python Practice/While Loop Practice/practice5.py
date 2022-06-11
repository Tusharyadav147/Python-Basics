"""5. Write a Python program that accepts a word from the user
and reverse it."""

word = input("Enter word to reverse it: ")
n = len(word)
m = n-1
reverse_word = ""
for i in range(0, n):
    reverse_word += word[m]
    m -= 1
print(reverse_word)