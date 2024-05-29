#!/usr/bin/python3

"""
Module 1. Real definition of a rectangle
Defines a rectangle
"""


class Rectangle:
    """
    Class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
    """

    def __init__(self, width=0, height=0):
        """
            Initializes rectangle area
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the private instance attribute width.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Setter for the private instance attribute width.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Getter for the private instance attribute height.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Setter for the private instance attribute height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
