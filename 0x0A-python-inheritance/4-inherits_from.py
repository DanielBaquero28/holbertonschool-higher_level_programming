#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ Returns True if obj is an instance of a class that inherited directly
    or indirectly """

    if type(obj) is a_class:
        return (False)
    return (isinstance(obj, a_class))
