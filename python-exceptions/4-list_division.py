#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    results = []
    for a, b in zip(my_list_1, my_list_2):
        try:
            result = a / b
        except ZeroDivisionError:
            result = None
        except TypeError:
            result = None
        finally:
            results.append(result)
        if b = 0:
            print("division by 0")
        if a is not int:
            print("wrong type")
        if a is not float:
            print("wrong type")
        if b is not int:
            print("wrong type")
        if b is not float:
            print("wrong type")
        if my_list_1 < list_length:
            print("out of range")
        if my_list_2 < list_length:
            print("out of range")
    return results
