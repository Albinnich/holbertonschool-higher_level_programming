#!/usr/bin/python3

"""
    The ''8. Rectangle'' module
"""


class Rectangle(BaseGeometry):
    """
    Class to inherit
    """

    def __init__(self, width, height):
        """
        Function writes rectangle
        """

        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
