#!/usr/bin/python3

def multiple_returns(sentence):
    tuplex = tuple(sentence)
    length = len(tuplex)
    first = tuplex[0]
    if length == 0:
        print("Length: 0 - First character: None")
    else:
        print(f"Length: {length} - First character: {first}")
