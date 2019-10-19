#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """ Subclass that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor method of Rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Gets the value of width with property decorator """
        return (self.__width)

    @width.setter
    def width(self, name, value):
        """ Sets the value of width with setter decorator """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))
        self.__width = value

    @property
    def height(self):
        """ Gets the value of height with property decorator """
        return (self.__width)

    @height.setter
    def height(self, name, value):
        """ Sets the value of height with setter decorator """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))
        self.__height = value

    @property
    def x(self):
        """ Gets the value of x with property decorator """
        return (self.__x)

    @x.setter
    def x(self, name, value):
        """ Sets the value of x with setter decorator """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))
        self.__x = value

    @property
    def y(self):
        """ Gets the value of y with property decorator """
        return (self.__y)

    @y.setter
    def y(self, name, value):
        """ Sets the value of y with setter decorator """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))
        self.__y = value
