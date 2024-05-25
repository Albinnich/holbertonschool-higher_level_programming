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

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Property to retrieve.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                any(i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Returns area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints stdout the square with character #.

        Args:
            size: If equal to 0 prints empty line
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
