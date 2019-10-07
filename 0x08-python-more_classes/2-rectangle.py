#!/usr/bin/python3
class Rectangle:
    """
    Class that defines a Rectangle.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves value of width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Sets the value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Retrieves value of height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Sets value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Returns area of the square.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Returns the perimeter of the square
        """
        return ((self.__width * 2) + (self.__height * 2))
