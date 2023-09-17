#!/usr/bin/python3
"""Base module
base class for my Rectangle class
"""

from . import base


class Rectangle(base.Base):
    """Rectangle class
    subclass of Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class
        constructor
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(height):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(y):
        self.__y = y
