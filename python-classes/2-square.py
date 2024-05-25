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

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) != int:
            raise TypeError
        if size < 0:
            raise ValueError
        self.__size = size
