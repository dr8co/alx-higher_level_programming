#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file and prints it.
    """

    with open(filename) as f:
        text = f.read()
        print(text, end="")
