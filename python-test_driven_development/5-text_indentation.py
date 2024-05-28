#!/usr/bin/python3

"""
    The ''4. Text indentation'' module.
    This module contains a function: text_indentation
"""


def text_indentation(text):
    """
        text_indentation - It prints a text with 2 new lines
        after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    print(text)
