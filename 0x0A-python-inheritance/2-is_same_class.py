#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ Returns True if obj is exactly an instance of a_class. """
    if not type(obj) is a_class:
        return (False)
    else:
        return (True)
