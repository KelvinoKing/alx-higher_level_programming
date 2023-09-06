#!/usr/bin/python3

""" print_square module
Prints a square using #
"""


def print_square(size):
    """ function prints a square using # signs

    args:
        size (int): size of square

    Raises:
        TypeError: if size is not an int
        ValueError: size is less than 0
    """

    if size is None:
        raise TypeError('size must be an integer')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        j = 0
        for j in range(size):
            print("#", end="")
        print()
