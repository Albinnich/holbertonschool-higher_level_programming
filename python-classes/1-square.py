#!/usr/bin/python3

"""
This module defines a class Square that defines a square.
"""


class Square:
    """
    This is a square class based on 0-square.py

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """
        Starts a new Square instance.

        Args:
        size(int): The size of the square.
        """
        self._size = size
