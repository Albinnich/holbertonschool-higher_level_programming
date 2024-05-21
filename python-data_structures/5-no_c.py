#!/usr/bin/python3

def no_c(my_string):
    my_new_string = my_string.translate( { ord("c") } )
    print(my_new_string)
