#!/usr/bin/python3
for i in range(0, 10):
    for k in range(i+1, 10):
        print("{:d}{:d}".format(i, k), end=', ' if i != 8 or k != 9 else "\n")
