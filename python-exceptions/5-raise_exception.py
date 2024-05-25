#!/usr/bin/python3

def raise_exception():
    raise Exception
    try:
        print("Exception has been raised")
    except Exception:
        return False
