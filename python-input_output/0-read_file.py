#!/usr/bin/python3

def read_file(filename=""):
    with open('UTF8.txt') as f:
        UTF8 = f.read()
        print(UTF8)
