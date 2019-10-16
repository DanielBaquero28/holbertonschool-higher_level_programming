#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ Prints in stdout nb_lines of the file. """
    line_number = 0
    with open(filename, encoding='utf-8') as my_file:
        if (nb_lines <= 0):
            my_file_read = my_file.read()
            print(my_file_read, end='')
        else:
            for a_line in my_file:
                if (line_number < nb_lines):
                    print(a_line, end='')
                    line_number += 1
