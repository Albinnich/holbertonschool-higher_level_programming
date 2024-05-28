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

    chars = ['.', '?', ':']
    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in chars:
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    print(result, end="")
