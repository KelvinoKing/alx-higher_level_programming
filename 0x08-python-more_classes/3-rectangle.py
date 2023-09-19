#!/usr/bin/python3
"""Rectangle
my class
"""


class Rectangle:
    """Rectangle
    defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """object constructor
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """returns area
        """
        return self.height * self.width

    def perimeter(self):
        """returns perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return self.height * 2 + self.width * 2

    def __str__(self):
        """prints the rectangle with character #
        """
        my_string = ""
        for j in range(self.height):
            for i in range(self.width):
                my_string += "#"
            if j != self.height - 1:
                my_string += "\n"

        return my_string
