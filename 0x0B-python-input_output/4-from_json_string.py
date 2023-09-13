#!/usr/bin/python3
"""json module
serializes and deserializes objects
"""

import json

"""from_json_string module
returns an object represented by a JSON string
"""


def from_json_string(my_str):
    """ deserializes a JSON string

    args:
        my_str: parameter
    Returns: object
    """

    return json.loads(my_str)
