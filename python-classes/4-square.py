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

    def size(self, value):
        """
        Property setter.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns area of the square.
        """
        return self.__size ** 2

    def __init__(self, size=0):
        """
        Initializes a new Square instance.
        """
