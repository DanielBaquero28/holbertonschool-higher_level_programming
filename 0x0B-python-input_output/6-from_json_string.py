#!/usr/bin/python3
import json


def from_json_string(my_str):
    """ Returns an object (Python data structure) represented by JSON string"""
    restored_data = json.loads(my_str)

    return (restored_data)
