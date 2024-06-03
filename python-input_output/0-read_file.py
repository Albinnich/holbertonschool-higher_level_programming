#!/usr/bin/python3

"""
    The ''0. Read file'' module
"""


def read_file(filename=""):
    """
    read_file function reads text file
    """

    with open("file.txt", "r", encoding="utf-8") as f:
        text = f.read()
        print(text)
