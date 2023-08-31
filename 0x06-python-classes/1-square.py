#!/usr/bin/python3
"""
Square class
"""


class Square:
    """Defines a square by attribute of size."""

    def __init__(self, size):
        """__init__ medhod to initialize class with a specified size.

        Args:
            size (int): Initializes the size of the square

        """
        self.__size = size
