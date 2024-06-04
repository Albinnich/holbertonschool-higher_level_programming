#!/usr/bin/python3i

"""
    The ''5. Save Object to a file'' module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - function to write an object to text file
    """
    my_list = list(my_obj)

    json_string = json.dumps(my_obj)

    with open(filename, 'w') as f:
        f.write(json_string)
