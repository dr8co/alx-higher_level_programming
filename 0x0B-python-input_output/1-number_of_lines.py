#!/usr/bin/python3

def number_of_lines(filename=""):
    """
    Returns the number of lines in a text file.
    """
    lines = 0
    with open(filename) as f:
        for _ in f:
            lines += 1
        return lines
