#!/usr/bin/python3

"""
    The ''10. Square #1'' module
"""


class Square:
    """
    Class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initializes size
        """

        super().__init__()
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Defines area
        """
        return self.__width * self.__height
