#!/usr/bin/python3

"""
This module writes a class Mylist that inherits from list
"""


class MyList(list):
    """
    A subclass of list that can print itself sorted

    Methods:
        print_sorted(self): Prints list in ascending sorted order
    """


    def print_sorted(self):
        """
        Prints the list but sorted in ascending order
        """
        print(sorted(self))
