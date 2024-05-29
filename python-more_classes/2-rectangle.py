#!/usr/bin/python3

"""
Module 2. Area and Perimeter
Defines area and perimeter fo rectangle
"""


class Rectangle:
    """
    Class Rectangle defines area and perimeter of rectangle
    - Private instance attributes: width and height
    - property and setter methods for width and height
    """

    def __init__(self, width=0, height=0):
        """
        Initializes rectangle area and perimeter
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the private instance attribute width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the private instance attribute width.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the private instance attribute height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the private instance attribute height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.width + self.height)
