#!/usr/bin/python3
"""Rectangle
my class
"""


class Rectangle:
    """Rectangle
    defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """object constructor
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return my_string
        for j in range(self.height):
            for i in range(self.width):
                my_string += str(self.print_symbol)
            if j != self.height - 1:
                my_string += "\n"

        return my_string

    def __repr__(self):
        """returns a string rep of the rectangle to be
        able to recreate a new instance by using eval()
        """
        return "{}({}, {})".format(
                type(self).__name__,
                self.width, self.height)

    def __del__(self):
        """deletes an instance of an the class
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on area

        args:
            rect_1 (Rectangle): first param
            rect_2 (Rectangle): second param
        """
        if  not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if  not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
