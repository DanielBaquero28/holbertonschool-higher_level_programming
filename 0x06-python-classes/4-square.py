#!/usr/bin/python3
class Square:
    """This is a class defining a square.
    """
    def __init__(self, size=0):
        """Declares the method where the size of the sqaure is defined.
        Args:
            param1 (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Declares the method where the area of a square is returned.
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """Declares the method where returns the value of the size of square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Declares the method where sets the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
