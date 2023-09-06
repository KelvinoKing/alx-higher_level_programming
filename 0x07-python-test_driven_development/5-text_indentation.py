#!/usr/bin/python3

""" text_indentation
Prints text with 2 new lines after each characters: . ? :
"""


def text_indentation(text):
    """ prints text in specified format

    args:
        text (string): text to be printed
    Raises:
        TypeError: if paramter is not str
    """

    if text is None:
        raise TypeError('text must be a string')
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    i = 0
    while i < len(text):
        if text[i] != '.' and text[i] != '?' and text[i] != ':':
            print(text[i], end="")
        else:
            print(text[i])
            print()
            if text[i + 1] == ' ':
                i += 2
                continue
        i += 1
