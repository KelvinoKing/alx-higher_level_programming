#!/usr/bin/python3

"""lookup module
Returns a list of an object's attributes
"""


def lookup(obj):
    """lookup function returns a list of attributes of it's parameters

    args:
        obj (obj): parameter of type obj

    Returns: a list
    """

    if not isinstance(obj, object):
        raise TypeError('Parameter must be an object')
    if obj is None:
        raise TypeError('Parameter must be an object')

    return dir(obj)
