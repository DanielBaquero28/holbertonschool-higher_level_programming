#!/usr/bin/python3
"""

Function's Name: say_my_name

Test command: python3 -m doctest -v ./tests/3-say_my_name.txt

"""
def say_my_name(first_name, last_name=""):
    """
    Prints first and last name.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
