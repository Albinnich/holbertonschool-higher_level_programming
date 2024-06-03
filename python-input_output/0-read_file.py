#!/usr/bin/python3

"""
    The ''0. Read file'' module
"""


def read_file(filename=""):
    """
    read_file function reads text file
    """

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
