#!/usr/bin/python3

"""
Module ''3. Same class or inherit from''
"""


def is_kind_of_class(obj, a_class):
    """
        is_kind_of_class - returns True if the object is an instance of
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
