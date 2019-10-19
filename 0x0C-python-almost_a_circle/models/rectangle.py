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
    def width(self, value):
        """ Sets the value of width with setter decorator """
        if not type(value) == int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the value of height with property decorator """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Sets the value of height with setter decorator """
        if not type(value) == int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Gets the value of x with property decorator """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ Sets the value of x with setter decorator """
        if not type(value) == int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Gets the value of y with property decorator """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ Sets the value of y with setter decorator """
        if not type(value) == int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Gets the value of the area of the rectangle """
        return (self.__width * self.__height)

    def display(self):
        """ Prints in stdout the rectangle with '#' """
        for i in range(self.__height):
            print("#" * self.__width)
