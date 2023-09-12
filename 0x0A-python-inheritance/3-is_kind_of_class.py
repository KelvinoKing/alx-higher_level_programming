#!/usr/bin/python3
"""is_kind_of_class module
checks if an object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """ function checks if obj is an instance of a_class

    args:
        obj (object): first parameter
        a_class: second parameter

    Return: True if obj is instance of a_class else False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
