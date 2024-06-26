#!/usr/bin/python3

"""
This module provides a function "add integer" that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int, float): The first number.
        b (int, float): The second number, defaults to 98.

    Returns:
        int: The sum of a and b, casted to integers.

    Raises:
        TypeError: if either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
