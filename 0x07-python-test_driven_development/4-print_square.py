#!/usr/bin/python3
"""
Function's name: print_square()

Test command: python3 -m doctest -v ./tests/4-print_square.txt
"""
def print_square(size):
    """
    Prints a square of the size you enter.
    Return:
    Square printed in '#'
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
