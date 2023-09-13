#!/usr/bin/python3
""" write_file module
writes a string to a text file
"""


def write_file(filename="", text=""):
    """function writes a sttring in a text file

    args:
        filename: name of file
        text: string to be writen

    Returns: number of characters writen
    """

    with open(filename, 'w', encoding="utf-8") as my_file:
        num_chars = my_file.write(text)

    return num_chars
