#!/usr/bin/python3
"""add_attribute module
A function that adds a new attribute to an object
"""


def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object if possible
    args:
        obj (object): object
        attribute: attribute
        value: value to set
    Raises:
        TypeError: if the attribute can't be set
    """

    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
