#!/usr/bin/python3
"""class module"""
import json


class Base:
    """base class of our programe"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constractore of our class."""
        if (id):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """confarm json string"""
        
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """convart jason to file"""

        if list_objs:
            list_objs = [i.to_dictionary() for i in list_objs]

        with open("{}.json".format(cls.__name__), 'w', encoding="UTF8") as fil:
            fil.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """return list of json string"""

        if json_string is None or not json_string:
            return []

        return ["{}".format(json.loads(json_string))]

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""

        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            dummy = Rectangle(1, 1)
        elif cls is Square:
            dummy = Square(1)
        else:
            dummy = None

        dummy.update(**dictionary)
        return dummy
