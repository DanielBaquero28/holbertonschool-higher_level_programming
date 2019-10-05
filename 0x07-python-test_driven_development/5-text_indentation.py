#!/usr/bin/python3
"""
Function's name: text_indentation

Testing command: python3 -m doctest -v ./tests/5-text_indentation.txt
"""
def text_indentation(text):
    """
    Prints 2 new lines after ".?:" characters.
    """
    special_characters = ".?:"
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = text[:]
    for i in special_characters:
        list_text = string.split(i)
        string = ""
        for j in list_text:
            j = j.strip(" ")
            string = j + i if string is "" else string + "\n\n" + j + i

    print(string[:-3], end="")
