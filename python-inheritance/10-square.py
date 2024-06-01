#!/usr/bin/python3

"""
    The ''10. Square #1'' module
"""

Rectangle = __import__('8-rectangle').Rectangle


class Square:
    """
    Class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initializes size
        """

        super().__init__(size, size)

    def __str__(self):
         """Return the square description."""
         return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

    def area(self):
        """
        Defines area
        """
        return self._Rectangle__width * self._Rectangle__height
