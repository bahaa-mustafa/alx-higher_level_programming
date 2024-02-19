#!/usr/bin/python3
"""Module of class"""


class MyList(list):
    """class inherits from list"""
    def print_sorted(self):
        """function print the list in sorted way"""
        print(sorted(self))
