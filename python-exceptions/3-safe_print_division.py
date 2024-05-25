#!/usr/bin/python3

def safe_print_division(a, b):
    result = a / b
    try:
        print("{:d}".format(result))
        return True
    except Exception:
        return False
