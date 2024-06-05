#!/usr/bin/env python3

"""
The ''2. Converting CSV Data to JSON Format'' module
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        json_data = json.dumps(data, indent=4)

        with open('data.json', 'w') as json_file:
            json_file.write(json_data)

        return True
    except FileNotFoundError:
        print("File not found.")
        return False
