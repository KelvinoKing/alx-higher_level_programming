#!/usr/bin/python3


def class_to_json(obj):
    """serialize class attributes to dictionary

    args:
        obj: class
    """
    return obj.__dict__
