#!/usr/bin/python3

""" add_integer

Adds two integers and return the result
"""


def add_integer(a, b=98):
    """ Adds two integers and return result

    args:
        a : first parameter
        b : second parameter
    Raises:
        TypeError: if parameters are not integers or float
    Returns: result of addition
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('a must be an integer')

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
