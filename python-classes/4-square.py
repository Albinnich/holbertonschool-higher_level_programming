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
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value


    def area(self):
        """
        Returns area of the square.
        """
        return self.__size ** 2
