#!/usr/bin/python3
""" Importing module json in order to manipulate it """
import json


class Base:
    """ Base Class """
    __nb_objects = 0
    def __init__(self, id=None):
        """ Constructor method of the class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns an empty list if list_dictionaries is equal to None, else
        returns JSON string representation it.
        """
        if list_dictionaries is None:
            return ("[]")
        if not type(list_dictionaries) == list:
            raise TypeError("list_dictionaries must be a list")
        for i in list_dictionaries:
            if not type(i) == dict:
                raise TypeError("Must be a list of dictionaries")

        string_json = json.dumps(list_dictionaries)
        return (string_json)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        desc = []
        with open(str(cls.__name__) + '.json', mode='w', encoding='utf-8') as my_file:
            if list_objs is None:
                my_file.write(Base.to_json_string(desc))
                return
            if not type(list_objs) == list:
                raise TypeError("list_objs must be a list of instances")
            for objs in list_objs:
                desc.append(objs.to_dictionary())

            return (my_file.write(Base.to_json_string(desc)))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None or json_string == "":
            return ("[]")
        if not type(json_string) == str and json_string is not None:
            raise TypeError("json_string must be a string")

        json_loads = json.loads(json_string)
        return (json_loads)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance of all attributes already set """
        dummy_instances = 0
        if cls.__name__ is 'Rectangle':
            dummy_instances = cls(5, 5, 5, 5, 5)
        elif cls.__name__ is 'Square':
            dummy_instances = cls(5, 5, 5, 5)
        else:
            raise TypeError("cls has to be of class Rectangle or Square")

        dummy_instances.update(**dictionary)
        return (dummy_instances)
