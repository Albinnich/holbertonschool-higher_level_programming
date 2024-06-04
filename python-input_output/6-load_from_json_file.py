#!/usr/bin/python3

"""
The ''6. Create object from a JSON file'' module
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file function to create an Object from json file
    """

    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
    return json.loads(read_data)
