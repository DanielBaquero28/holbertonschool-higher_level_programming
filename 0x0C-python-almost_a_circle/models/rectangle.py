#!/usr/bin/python3
""" Imports module Base """
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
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print("", end=" ")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ Magic method that returns an object string representation """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                        self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        num_arg = 0
        if len(args) != 0 and args:
            for arg in args:
                if num_arg == 0:
                    self.id = args[0]
                elif num_arg == 1:
                    self.__width = args[1]
                elif num_arg == 2:
                    self.__height = args[2]
                elif num_arg == 3:
                    self.__x = args[3]
                elif num_arg == 4:
                    self.__y = args[4]
                num_arg += 1
            return

        for key in kwargs:
            if key == "id":
                self.id = kwargs["id"]
            if key == "width":
                self.__width = kwargs["width"]
            if key == "height":
                self.__height = kwargs["height"]
            if key == "x":
                self.__x = kwargs["x"]
            if key == "y":
                self.__y = kwargs["y"]
