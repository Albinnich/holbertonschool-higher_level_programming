#!/usr/bin/python3

"""
    The ''13. Can I?'' module
"""


def add_attribute(obj, attribute, value):
    """
    Function add_attribute adds new atribute to an object
    """
    if not isinstance(obj, type):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
