#!/usr/bin/python3
def no_c(my_string):
    for element in my_string:
        if element == 'C' or element == 'c':
            print("", end="")
        else:
            print(element, end="")
