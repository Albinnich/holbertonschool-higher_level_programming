#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    elif roman_string is not str:
        return 0
    else:
        return int(roman_string)
