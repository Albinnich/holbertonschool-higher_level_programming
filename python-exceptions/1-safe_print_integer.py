#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError:
        return False
    else:
        print("{0:d}".format(value))
        return True
