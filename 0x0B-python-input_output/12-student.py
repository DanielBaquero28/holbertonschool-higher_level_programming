#!/usr/bin/python3
class Student:
    """ Class that defines attributes of a Student. """
    desc = {}
    complete_list = {}

    def __init__(self, first_name, last_name, age):
        """ Method constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if hasattr(self, '__dict__'):
            desc = self.__dict__.copy()

        if type(attrs) is list:
            for element in attrs:
                if type(element) is not str:
                    return (desc)

            for key, value in ((range(len(attrs))), desc):
                if attrs[key] == value:
                    complete_list = desc[value]
                    return (complete_list)

        return (desc)
