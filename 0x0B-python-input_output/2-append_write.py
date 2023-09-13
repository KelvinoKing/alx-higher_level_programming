#!/usr/bin/python3
""" append_write module
appends a string at end of file
"""


def append_write(filename="", text=""):
    """function appends text at end of file'

    args:
        filename: name of file
        text: text to be added

    Returns: number of chars added
    """

    with open(filename, 'a', encoding="utf-8") as my_file:
        num_chars = my_file.write(text)

    return num_chars
