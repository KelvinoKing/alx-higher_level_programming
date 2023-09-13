#!/usr/bin/python3
"""json module
serializes an object and saves it in a file
"""

import json

"""save_to_json_file
saves serialized obj (string) into file
"""


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON rep

    args:
        my_obj: object to be serialized
        filename: text file
    """

    with open(filename, 'w', encoding='utf-8') as my_file:
        json.dump(my_obj, my_file)
