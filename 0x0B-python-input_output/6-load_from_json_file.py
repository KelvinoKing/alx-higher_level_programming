#!/usr/bin/python3
"""json module
deserialize an object
"""

import json

"""load_from_json_file
creates an Object from a JSON file
"""


def load_from_json_file(filename):
    """creates an Object from a JSON file

    args:
        filename: name of JSON file
    """

    with open(filename, encoding="utf-8") as my_file:
        data = json.load(my_file)

    return data
