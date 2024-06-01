#!/usr/bin/python3

"""
    The ''12. My integer'' module
"""


class MyInt(int):
    """
    Class that inherits from int
    """

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
