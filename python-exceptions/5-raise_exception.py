#!/usr/bin/python3

def raise_exception(value):
    if type(value) not in [int, float]:
        raise TypeError
