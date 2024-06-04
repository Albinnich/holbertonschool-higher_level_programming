#!/usr/bin/python3

"""
The ''9. Student to JSON'' module
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes with first_name, last_name and age
        """
        def to_json(self):
            """
            Retrieves a dictionary representation of the Student instance
            """
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
