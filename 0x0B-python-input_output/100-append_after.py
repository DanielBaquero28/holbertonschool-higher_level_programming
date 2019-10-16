#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line
    containing a specific string.
    """

    with open(filename, encoding='utf-8') as my_file:
        extend_string = ''
        for line in my_file:
            if search_string in line:
                extend_string += line + new_string
            else:
                extend_string += line

    with open(filename, mode='w', encoding= 'utf-8') as my_file:
        my_file.write(extend_string)
