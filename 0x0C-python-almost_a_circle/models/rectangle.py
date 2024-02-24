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
        self.check_value("width", value)
        self.__width = value

    @property
    def height(self):
        """getter and setter for reactangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.check_value("height", value)
        self.__height = value

    @property
    def x(self):
        """getter and setter for reactangle x"""
        return self.__x

    @x.setter
    def x(self, value):
        self.check_value("x", value, False)
        self.__x = value

    @property
    def y(self):
        """getter and setter for reactangle y"""
        return self.__y

    @y.setter
    def y(self, value):
        self.check_value("y", value, False)
        self.__y = value

    def check_value(self, name, value, not_zero = True):
        """check if value is number integer bigger than 0 or equal"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0 and not_zero:
            raise ValueError("{} must be > 0".format(name))
        elif value <= 0 and not_zero == False:
            raise ValueError("{} must be >= 0".format(name))
