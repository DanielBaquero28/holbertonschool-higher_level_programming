#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_list = list(a_dictionary.keys())
    for val in new_list:
        if value == a_dictionary.get(val):
            del a_dictionary[val]

    return (a_dictionary)
