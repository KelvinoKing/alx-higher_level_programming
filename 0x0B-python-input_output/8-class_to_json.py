#!/usr/bin/python3
"""class_to_json
returns a dictionary rep of a class
"""


def class_to_json(obj):
    """serialize class attributes to dictionary

    args:
        obj: class
    """
    return obj.__dict__
