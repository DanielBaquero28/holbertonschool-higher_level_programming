#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            character = chr(ord(i) - 32)
        else:
            character = i
        print("{}".format(character), end="")
    print("")
