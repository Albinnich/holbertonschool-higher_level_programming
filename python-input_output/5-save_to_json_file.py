#!/usr/bin/python3i

"""
    The ''5. Save Object to a file'' module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - function to write an object to text file
    """
    with open(filename, 'w') as file:
        file.write(my_obj)
