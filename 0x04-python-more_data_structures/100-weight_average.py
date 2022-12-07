#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    returns the weighted average of all integers in a list of tuples.
    """
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    avg = 0
    size = 0
    for tupl in my_list:
        avg += (tupl[0] * tupl[1])
        size += tupl[1]
    return (avg / size)
