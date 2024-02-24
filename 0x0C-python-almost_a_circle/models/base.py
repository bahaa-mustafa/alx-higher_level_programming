#!/usr/bin/python3
"""class module"""


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
