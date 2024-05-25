#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    results = []
    for a, b in zip(my_list_1, my_list_2):
        try:
            result = a / b
        except ZeroDivisionError:
            result = 0
        except TypeError:
            result = None
        finally:
            results.append(result)
    if 0 in my_list_2:
        print("division by 0")
    for a, b in zip(my_list_1, my_list_2):
        if not (type(a) in (int, float) and type(b) in (int, float)):
            print("wrong type")
    if len(results) < list_length:
        print("out of range")
    return results
