"""3. Write a Python program to guess a number between 1 to 9.
Note : User is prompted to enter a guess. If the user guesses
wrong then the prompt appears again until the guess is
correct, on successful guess, user will get a "Well guessed!"
message, and the program will exit"""
n = 0
while n >= 0:
    n = int(input("Enter a number :"))
    if n>= 1  and n <= 9:
        print("Well Guessed !")
        break
    else:
        pass
