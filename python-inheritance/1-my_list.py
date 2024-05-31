#!/usr/bin/python3

"""
This module writes a class Mylist that inherits from list
"""


def print_sorted(self):
    """
    Prints the list but sorted
    """

    if not isinstance(self, int):
        raise TypeError

    n = len(self)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if self[j] > self[j + 1]:
                self[j], self[j + 1] = self[j + 1], self[j]
