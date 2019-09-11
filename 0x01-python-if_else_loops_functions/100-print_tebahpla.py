#!/usr/bin/python3
for letter in range(ord('z') + 1, ord('a')):
    if (ord(letter) % 2 != 0):
        character = chr(ord(letter) - 32)
        print("{}".format(character), end="")
    else:
        character = letter
        print("{}".format(character), end="")
