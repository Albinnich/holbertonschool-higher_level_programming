#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    new_list = replace_in_list(my_list, idx, new_element)
    if 0 > idx > len(my_list):
        return my_list
    else:
        return new_list
