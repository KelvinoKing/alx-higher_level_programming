#!/usr/bin/python3
""" Rectangle module
It is a class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class
    inherits from Rectangle class
    """
    def __init__(self, size):
        """class function
        constructor

        args:
            size (int): first param
        """
        super().integer_validator("size", size)
        super().__init__(size, size)

        self.__size = size

    def area(self):
        """calculates the area of rectangle
        """
        return self.__size * self.__size
