#!/usr/bin/python3

"""
===============================
module with the class Student
===============================
"""


class Student:
    """
    Class with methods to_json for retrieves dictionary
    """

    def __init__(self, first_name, last_name, age):
        """
        Method to initialize all attributes
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
