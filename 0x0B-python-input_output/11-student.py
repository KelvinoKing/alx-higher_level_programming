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

    def to_json(self, attrs=None):
        """to_json method
        returns a dictionary rep of class attributes
        """

        obj_dict = self.__dict__
        if attrs is None:
            return self.__dict__
        else:
            filterd_dict = {}
            for att in attrs:
                if hasattr(self, att):
                    filterd_dict[att] = obj_dict[att]
            return filterd_dict

    def reload_from_json(self, json):
        """replaces attributes
        """
        for i, j in json.items():
            if hasattr(self, i):
                setattr(self, i, j)
