#!/usr/bin/python3

def best_score(a_dictionary):
    """
    returns a key with the biggest integer value.
    """
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    ret = list(a_dictionary.keys())[0]
    big = a_dictionary[ret]
    for key, val in a_dictionary.items():
        if val > big:
            big = val
            ret = key
    return ret
