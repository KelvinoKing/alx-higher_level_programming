#!/usr/bin/python3
"""
Square class
"""


class Square:
    """The class uses setters and getter methods to set and retrive the size"""

    def __init__(self, size=0):
        """__init__ method to initialize value

        args:
            value (int): value of square

        """
        self.size = size

    @property
    def size(self):
        """ size method returns the value of the square

        size(value) sets the value of square

        args:
            value (int): for the setter
        Returns: value of square

        Raises:
            TypeError: if value is not int
            ValueError: if value is < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area method calculates the area of square

        Returns: area of square
        """

        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with character #"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                j = 0
                for j in range(self.__size):
                    print("#", end="")
                print()
