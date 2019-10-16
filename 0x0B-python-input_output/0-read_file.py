#!/usr/bin/python3
def read_file(filename=""):
    """ Prints file in stdout """
    with open(filename, encoding='utf-8') as my_file:
        my_file_read = my_file.read()
        print(my_file_read, end="")
