#!/usr/bin/python3

"""
This module defines a class Square that defines a square by its size.
"""


class Square:
    """
    This class represents a square.

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
