#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """a subclass of list"""
    pass

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(list(self)))
