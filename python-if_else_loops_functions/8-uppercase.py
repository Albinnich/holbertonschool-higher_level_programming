#!/usr/bin/python3
def uppercase(str):
    new = ''
    for i in str:
        if (ord(i) > 96 and ord(i) < 123):
            new = new + chr(ord(i) - 32)
    return new
print("{}".format(uppercase()))
