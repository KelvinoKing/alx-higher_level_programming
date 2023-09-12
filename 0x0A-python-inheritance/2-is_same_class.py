#!/usr/bin/python3
"""is_same_class module
Checks if an object is an instance of specified class
"""


def is_same_class(obj, a_class):
    """ function checks if obj is instance of a_class

    args:
        obj (object): object passed
        a_class: class passed

    Returns: True if obj is instace of a_class otherwise False
    """

    if type(obj) is a_class:
        return True
    else:
        return False
