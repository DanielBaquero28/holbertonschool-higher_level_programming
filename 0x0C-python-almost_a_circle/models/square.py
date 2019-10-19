#!/usr/bin/python3
""" Imports module rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Child class that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor method for Square """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Prints the string object representation """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))
