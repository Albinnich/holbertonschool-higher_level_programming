#!/usr/bin/python3

"""
    The ''7. Integer validator'' module
"""

class BaseGeometry:
    """
    Class that defines area
    """

    def area(self):
        """
        Defines area with exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
