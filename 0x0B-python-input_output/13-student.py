#!/usr/bin/python3
class Student:
    """ Class that defines attributes of a Student. """
    desc = {}

    def __init__(self, first_name, last_name, age):
        """ Method constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """

        complete_list = {}

        if hasattr(self, '__dict__'):
            desc = self.__dict__.copy()

        if type(attrs) is list:
            for element in attrs:
                if type(element) is not str:
                    return (desc)

            for key in range(len(attrs)):
                for value in desc:
                    if attrs[key] == value:
                        complete_list[value] = desc[value]
            return (complete_list)

        return (desc)

    def reload_from_json(self, json):
        """ Replaces all the attributes of the Student instance """
        for attr in json:
            self.__dict__[attr] = json[attr]
