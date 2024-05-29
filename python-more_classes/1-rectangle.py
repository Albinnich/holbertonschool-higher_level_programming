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

        if width not isinstance(type, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if height not isinstance(type, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return self.width*self.height


print(area())
