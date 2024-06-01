#!/usr/bin/python3

def add_attribute(obj, attribute, value):
    if hasattr(obj, attribute):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
