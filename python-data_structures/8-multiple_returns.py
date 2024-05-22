#!/usr/bin/python3

def multiple_returns(sentence):
    tuplex = tuple(sentence)
    length = len(tuplex)
    first = tuplex[0]
    print(f"Length: {length} - First character: {first}")
