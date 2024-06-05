#!/usr/bin/python3

"""
The ''10. Student to JSON with filter'' module
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes with first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance
        """
        if attrs is str:
            return self.__dict__
