#!/usr/bin/python3
def number_of_lines(filename=""):
    """ Returns the number of lines of the filename. """
    lines = 0
    with open(filename, encoding='utf-8') as my_file:
        for line_number in my_file:
            lines += 1

    return (lines)
