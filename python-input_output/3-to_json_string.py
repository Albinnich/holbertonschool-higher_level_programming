#!/usr/bin/python3

"""
    The ''To JSON string" module
"""

import json

def to_json_string(my_obj):
    """
    to_json_string function returns JSON representation of string
    """

    with open(my_obj, "w") as file:
        json.dump(my_obj, file)
