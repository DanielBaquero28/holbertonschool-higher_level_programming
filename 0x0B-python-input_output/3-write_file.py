#!/usr/bin/python3
def write_file(filename="", text=""):
    """ Writes text into a filename.

    Return: Number of characters of text.

    """
    with open(filename, mode='w', encoding='utf-8') as my_file:
        my_file.write(text)
        count = 0
        for char in text:
            count += 1

        return (count)
