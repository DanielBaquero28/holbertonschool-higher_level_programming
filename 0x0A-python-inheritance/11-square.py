#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Inherits from BaseGeometry. """
    def __init__(self, size):
        """ Constructor method """
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Returns the area of the square. """

        return (super().area())

    def __str__(self):
        """ Prints information about the square. """
        return (super().__str__())
