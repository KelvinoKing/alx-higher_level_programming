#!/usr/bin/python3
"""append_after
appends a line of text after a specified string
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after search string found
    Args:
        filename (str): path to filename
        search_string (str): search string
        new_string (str): string to insert
    """
    new_lines = []
    with open(filename, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)

    with open(filename, 'w', encoding='utf-8') as f:
        for line in new_lines:
            f.write(line)
