#!/usr/bin/python3
class MyInt(int):
    """ Inherits from int. """
    def __eq__(self, other):
        """ Changes it's use to != """
        return (int.__ne__(self, other))

    def __ne__(self, other):
        """ Changes it's use to == """
        return (int.__eq__(self, other))
