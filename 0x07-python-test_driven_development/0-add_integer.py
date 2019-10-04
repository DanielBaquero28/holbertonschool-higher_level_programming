#!/usr/bin/python3
"""

Function Name: add_integer().

Test command: python3 -m doctest -v ./tests/0-add_integer.txt

"""


def add_integer(a, b=98):
    """

    Calculates the sum of it's arguments.

    Return:
    Sum of int a and int b.
    """
    sum = 0

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    c = int(a)
    d = int(b)

    sum = c + d
    return (sum)
