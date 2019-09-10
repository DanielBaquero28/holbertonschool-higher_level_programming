#!/usr/bin/python3
for i in range(ord("a"), ord("z") + 1):
    if(i == 101 or i == 113):
        continue
    else:
        print("{:s}".format(chr(i)), end="")
