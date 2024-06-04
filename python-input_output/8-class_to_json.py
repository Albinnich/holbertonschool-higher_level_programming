#!/usr/bin/python3

"""
The ''8. Class to JSON'' module
"""

import json


def class_to_json(obj):
    """
    class_to_json function that returns dictionary description
    """

    result = {}
    for attr_name, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
            result[attr_name] = attr_value
    return result        
