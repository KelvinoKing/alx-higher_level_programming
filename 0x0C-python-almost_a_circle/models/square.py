#!/usr/bin/python3
"""Square class
inherits from the Rectangle class
"""
from . import rectangle


class Square(rectangle.Rectangle):
    """imports from the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """constructor for the square class
        args:
            size (int): width or height
            x (int):
            y (int):
            id (int): object id
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a string rep of Square class
        """
        return "[{}] ({}) {}/{} - {}".format(
                type(self).__name__,
                self.id, self.x, self.y, self.width)
