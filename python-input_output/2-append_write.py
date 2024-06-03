#!/usr/bin/python3

"""
    The ''2. Append to a file'' module
"""


def append_write(filename="", text=""):
    """
    append_write function to append a string
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
