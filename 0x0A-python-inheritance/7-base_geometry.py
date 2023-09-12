#!/usr/bin/python3
"""BaseGeometry module
It is a class
"""


class BaseGeometry(object):
    """BaseGeometry class
    """
    def __init__(self):
        """class function
        constructor
        """
        pass

    def area(self):
        """area function
        not implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates the value passed

        args:
            name (string): name of object
            value (int): value passed

        Raises:
            TypeError: if value is not integer
            ValueError: if value is not greater than 0
        """

        if value is None:
            raise TypeError("{} must be an integer".format(name))
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = name
        self.value = value
