#!/usr/bin/python3

def best_score(a_dictionary):
    maxscore = max(zip(a_dictionary.values(), a_dictionary.keys()))[1]
    return maxscore
