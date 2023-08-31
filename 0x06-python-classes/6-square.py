#!/usr/bin/python3
"""Square class
Square class defination with private size and position and public area
can access and update size and position
"""


class Square:
    """
    square defination
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square
        Attributes:
            __size(int): side of a square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if type(value) is not int:
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):

        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates Area of a square
        """
        return (self.__size)**2

    def my_print(self):
        if self.__size == 0:
            print()
            return None
        else:
            print("\n" * self.__position[1], end='')

            for rows in range(self.__size):
                spaces = " " * self.__position[0]
                hashes = "#" * self.__size
                print(spaces + hashes)
