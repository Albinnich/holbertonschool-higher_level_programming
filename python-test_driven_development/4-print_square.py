#!/usr/bin/python3

"""
    The ''3. Print a square'' module.
    This module contains a function: print_square
"""


def print_square(size):
    """
        print_square - It prints a square with character #.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")

    print("#", end='')
