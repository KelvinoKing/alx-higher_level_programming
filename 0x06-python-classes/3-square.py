#!/usr/bin/python3
"""
Square class
"""


class Square:
    """Square class that calculates the area."""

    def __init__(self, size=0):
        """ __init__ method for initializing size.

        args:
            size (int): size of the square
        Raises:
            TypeError: if size is not int
            ValueError: if size is less than zero

        """

        if type(size) is not int:
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ area() method returns the area of square.

        Returns:
            current square area

        """

        return self.__size * self.__size
