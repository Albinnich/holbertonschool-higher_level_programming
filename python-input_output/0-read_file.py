#!/usr/bin/python3

"""
    The ''0. Read file'' module
"""

def read_file(filename=""):
    """
    read_file function reads text file
    """

    with open('UTF8.txt') as f:
        UTF8 = f.read()
        print(UTF8)
