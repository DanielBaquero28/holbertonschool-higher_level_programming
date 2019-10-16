#!/usr/bin/python3
def class_to_json(obj):
    """ Returns the dictionary description with simple data structure. """
    desc = {}
    if hasattr(obj, '__dict__'):
        desc = obj.__dict__.copy()

    return (desc)
