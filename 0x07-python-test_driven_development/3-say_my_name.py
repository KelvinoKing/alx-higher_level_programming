#!/usr/bin/python3
""" say_my_name module
Prints out a sentence using the passed parameters
"""


def say_my_name(first_name, last_name=""):
    """ functions prints out a sentence using the passed params

    args:
        first_name (str): first parameter
        last_name (str): second parameter

    Raises:
        TypeError: wrong type of param passed
    """

    if first_name is None:
        raise TypeError('first_name must be a string')
    if last_name is None:
        raise TypeError('last_name must be a string')

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print("My name is {} {}".format(first_name, last_name))
