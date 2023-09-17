#!/usr/bin/python3
"""base
my class
"""


class Base(object):
    """Base class
    base class for all other classes
    """
    __no_objects = 0

    def __init__(self, id=None):
        """__init__ is a constructor for
        base class
        """

        if id is not None:
            self.id = id
        else:
            Base.__no_objects += 1
            self.id = Base.__no_objects
