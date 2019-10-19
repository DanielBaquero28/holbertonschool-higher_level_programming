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

    @property
    def size(self):
        """ Gets the value of size with property decorator"""
        return (self.width)

    @size.setter
    def size(self, value):
        """ Sets the value of size with setter decorator """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns an key/value argument to each corresponding method """
        num_arg = 0
        if len(args) != 0 and args:
            for arg in args:
                if num_arg == 0:
                    self.id = args[0]
                elif num_arg == 1:
                    self.size = args[1]
                elif num_arg == 2:
                    self.x = args[2]
                elif num_arg == 3:
                    self.y = args[3]
                num_arg += 1
            return

        for key in kwargs:
            if key == "id":
                self.id = kwargs["id"]
            if key == "size":
                self.size = kwargs["size"]
            if key == "x":
                self.x = kwargs["x"]
            if key == "y":
                self.y = kwargs["y"]
