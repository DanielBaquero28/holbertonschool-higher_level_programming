#!/usr/bin/python3
def lookup(obj):
    """ Returns a list of available attributes and methods of obj. """

    return (list(dir(obj)))
