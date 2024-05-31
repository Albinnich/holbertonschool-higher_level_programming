#!/usr/bin/python3

"""
The ''Exact same object'' module
"""


def is_same_class(obj, a_class):
    """
        is_same_class - returns exact object type
    """

    if isinstance(obj, a_class):
        return True
    if not isinstance(obj, a_class):
        return False
