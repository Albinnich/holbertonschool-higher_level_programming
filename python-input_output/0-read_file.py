#!/usr/bin/python3

"""
    The ''0. Read file'' module
"""


def read_file(filename=""):
    """
    read_file function reads text file
    """

    with open('my_file_0.txt', encoding="utf-8") as f:
        my_file_0 = f.read()
        print(my_file_0)
