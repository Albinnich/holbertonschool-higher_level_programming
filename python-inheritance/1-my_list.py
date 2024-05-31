#!/usr/bin/python3

"""
This module writes a class Mylist that inherits from list
"""


class MyList(list):
    """
    A subclass of list that can print itself sorted
    """


    def print_sorted(self):
        """
        Prints the list but sorted
        """
        print(sorted(self))
