#!/usr/bin/python3
"""inherits_from module
checks if the object is an instance of a class
"""


def inherits_from(obj, a_class):
    """checks if obj is an instance of a_class

    args:
        obj: first parameter
        a_class: second parameter

    Returns: True if the object is an instance of a class that inherited
            directly or indirectly from specified class
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
