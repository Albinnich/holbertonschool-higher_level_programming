#!/usr/bin/python3

def max_integer(my_list=[]):
    largest = my_list
    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]
    return largest
