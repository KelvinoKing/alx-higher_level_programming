#!/usr/bin/python3

"""json module
serializes an object
"""
import json

"""to_json_string
returns a JSON representation of an object
"""


def to_json_string(my_obj):
    """function serializes my_obj

    args:
        my_obj: object parameter
    Returns: JSON representation of my_obj
    """

    return json.dumps(my_obj)
