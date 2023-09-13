#!/usr/bin/python3
""" read_file module
reads a text file
"""


def read_file(filename=""):
    """reads a text file

    args:
        filename: file name
    """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
