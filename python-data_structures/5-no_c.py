#!/usr/bin/python3

def no_c(my_string):
    character_to_remove = "c"
    translation_table = str.maketrans("", character_to_remove)
    new_string = text.translate(translation.table)
    print(new_string)
