#!/usr/bin/python3
"""
Square class
"""


class Square:
    """Creates a square class and initializes size."""

    def __init__(self, size=0):
        """ __init__ method initializes square.

        args:
            size (int): size of the square

        Raises:
            TypeError: if size is not an int
            ValueError: if size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
