#!/usr/bin/python3

"""
    The ''8. Rectangle'' module
"""


class BaseGeometry:
    """
    Class to represent basic geometric shapes
    """


    def area(self):
        """
        Public instance method that raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates the value
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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

print(issubclass(Rectangle, BaseGeometry))
