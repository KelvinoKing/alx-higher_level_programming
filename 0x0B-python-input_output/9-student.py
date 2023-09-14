#!/usr/bin/python3
"""Student class
"""


class Student(object):
    """Student class
    defines a student
    """

    def __init__(self, first_name, last_name, age):
        """__init__
        class constructor with specified attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to_json method
        returns a dictionary rep of class attributes
        """
        return self.__dict__
