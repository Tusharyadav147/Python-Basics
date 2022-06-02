"""Write a function that stutters a word as if someone is struggling to read it. The
first two letters are repeated twice with an ellipsis ... and space after each, and then the
word is pronounced with a question mark ?."""

"""def stutters(word):
    s = word[:2]
    return (2*(s + "......")) +" "+ word + "?"

if __name__ == "__main__":
    word = input("type a word:")
    print(stutters(word))"""

"""2.Create a function that takes an angle in radians and returns the corresponding
angle in degrees rounded to one decimal place."""

def radians_to_degrees(radians):
    degree = (radians*180)
    return "radians_to_degrees {}".format(radians) + ra