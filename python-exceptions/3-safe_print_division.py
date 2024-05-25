#!/usr/bin/python3

def safe_print_division(a, b):
    result = a / b
    try:
        print("Inside result: {}".format(result))
        return True
    except ZeroDivisionError:
        return None
    finally:
        return result
