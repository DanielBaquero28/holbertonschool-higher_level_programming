#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """ Creates an Object from a “JSON file”. """
    with open(filename, encoding='utf-8') as my_file:
        restored_data = json.load(my_file)

        return (restored_data)
