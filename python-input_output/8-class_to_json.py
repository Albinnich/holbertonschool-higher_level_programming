#!/usr/bin/python3

"""
The ''8. Class to JSON'' module
"""


def class_to_json(obj):
    """
    class_to_json function that returns dictionary description
    """
    return obj.__dict__
