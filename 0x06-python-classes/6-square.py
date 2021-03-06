#!/usr/bin/python3
class Square:
    """This is a class defining a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Declares the method where the size of the sqaure is defined.
        Args:
            param1 (int): The size of the square
        """
        self.size = size
        self.position = position

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

        self.__size = value

    @property
    def position(self):
        """Declares a method that returns the value of the position.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Declares a method that sets the position.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Declares the method where the area of a square is returned.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Declares the method where the square is printed in stdout with #
        """
        if self.size == 0:
            print()
        else:
            for i in range(0, self.position[1]):
                print()
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                for n in range(self.__size):
                    print("#", end='')
                print()
