#!/usr/bin/python3

"""
    The ''1. Write to a file'' module
"""


def write_file(filename="", text=""):
    """
    write_file function writes a string to text file
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
