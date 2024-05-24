#!/usr/bin/python3

def common_elements(set_1, set_2):
    first_set = set(set_1)
    second_set = set(set_2)

    if (first_set & second_set):
        print(first_set & second_set)
