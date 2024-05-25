#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        res = my_list[:x]
        for i in range(x):
            print("{:d}".format(my_list[count]), end='')
            count += 1
        print()
        return count
    except IndexError:
        print()
        return count
