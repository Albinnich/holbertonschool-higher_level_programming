#!/usr/bin/python3

"""
    The ''5. Save Object to a file'' module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - function to write an object to text file
    """
    json.dump(my_obj, filename)
