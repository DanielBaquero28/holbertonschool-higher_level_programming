#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """ Writes an Object to a text file, using a JSON representation. """
    with open(filename, mode='w', encoding='utf-8') as my_file:
        json_object = json.dumps(my_obj)
        my_file.write(json_object)
