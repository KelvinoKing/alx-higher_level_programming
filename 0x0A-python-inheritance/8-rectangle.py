#!/usr/bin/python3
""" BaseGeometry module
It is a class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class
    inherits from BaseGeometry class
    """
    def __init__(self, width, height):
        """class function
        constructor

        args:
            width (int): first param
            height (int): second param
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
