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

if __name__ == "__main__":
    s = Square(5)

    print(s)
    print(dir(s))

    try:
        print("Square: {}".format(s.size))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        s2 = Square(0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
