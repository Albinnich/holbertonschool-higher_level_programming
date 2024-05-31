#!/usr/bin/python3

"""
Module ''4. Only sub class of''
"""


def inherits_from(obj, a_class):
    """
        inherits_from - returns True if the object is an
        instance of a class that inherited
        (directly or indirectly) from the specified class
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
