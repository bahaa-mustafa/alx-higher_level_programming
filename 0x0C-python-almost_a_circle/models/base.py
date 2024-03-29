#!/usr/bin/python3
"""class module"""
import json
import csv


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

        if json_string is None or json_string == '[]':
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == 'Rectangle':
                dummy = cls(1, 1)
            else:
                dummy = cls(1)

            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        try:
            with open("{}.json".format(cls.__name__), 'r') as fil:
                list_inst = Base.from_json_string(fil.read())
                return [cls.create(**lis) for lis in list_inst]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save file as csv file"""
        with open("{}.csv".format(cls.__name__), 'w', newline="") as fil:
            if list_objs is None or list_objs == []:
                fil.write("[]")
            else:
                if cls.__name__ == 'Rectangle':
                    file_args = ["id", "width", "height", "x", "y"]
                else:
                    file_args = ["id", "size", "x", "y"]
                saver = csv.DictWriter(fil, fieldnames=file_args)
                for obj in list_objs:
                    saver.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """load list from csv file"""
        try:
            with open("{}.csv".format(cls.__name__), 'r', newline="") as fil:
                if cls.__name__ == 'Rectangle':
                    file_args = ["id", "width", "height", "x", "y"]
                else:
                    file_args = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(fil, fieldnames=file_args)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                        for d in list_dicts]
                return [cls.create(**lis) for lis in list_dicts]
        except IOError:
            return []
