#!/usr/bin/env python3

"""
0. Basic Serialization
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    serialize_and_save_to_file - function to serialize and save data to file
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def load_and_deserialize(filename):
    """
    load_and_deserialize - function to load and deserialize data from specified file
    """
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data
