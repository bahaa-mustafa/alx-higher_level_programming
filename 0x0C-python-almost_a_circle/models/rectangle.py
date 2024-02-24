#!/usr/bin/python3
"""class module"""


from models.base import Base


class Rectangle(Base):
    """reactangle class inherits from base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """define faces of reactangle.
        Args:
            width: reactangle width
            height: reactangle height
            x: instance value
            y: instance value
        Return: no return
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter and setter for reactangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """getter and setter for reactangle width"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """getter and setter for reactangle width"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """getter and setter for reactangle width"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
