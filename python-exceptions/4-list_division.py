#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    results = []
    for i in range(list_length):
        try:
            a = my_list_1[i] if i < len(my_list_1) else None
            b = my_list_2[i] if i < len(my_list_2) else None

            if type(a) not in (int, float) or type(b) not in (int, float):
                print("wrong type")
                results.append(0)
                continue

            if b == 0:
                print("division by 0")
                results.append(0)
                continue

            result = a / b
            results.append(result)
        except IndexError:
            print("out of range")
            results.append(0)
        except ZeroDivisionError:
            print("division by 0")
            results.append(0)
    return results
