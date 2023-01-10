#!/usr/bin/python3

def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file and return
    the number of characters added.
    """

    with open(filename, 'a') as f:
        return f.write(text)
