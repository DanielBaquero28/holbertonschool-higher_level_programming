#!/usr/bin/python3
def multiple_returns(sentence):
    len_string = len(sentence)
    if len_string == 0:
        first_character = "None"
    else:
        first_character = sentence[0]

    return (len_string, first_character)
