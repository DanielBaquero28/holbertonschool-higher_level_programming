#!/usr/bin/python3
def append_write(filename="", text=""):
    """ Appends a string at the end of a text file. """
    with open(filename, mode='a', encoding='utf-8') as my_file:
        count = 0
        my_file.write(text)
        for char in text:
            count += 1

        return (count)
