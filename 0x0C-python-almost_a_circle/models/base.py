#!/usr/bin/python3
"""base
my class
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
