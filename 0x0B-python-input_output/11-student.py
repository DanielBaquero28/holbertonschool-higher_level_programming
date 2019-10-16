#!/usr/bin/python3
class Student:
    """ Class that defines attributes of a Student. """
    desc = {}
    def __init__(self, first_name, last_name, age):
        """ Method constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a dictionary representation of a Student instance """
        if hasattr(self, '__dict__'):
            desc = self.__dict__.copy()

        return (desc)
