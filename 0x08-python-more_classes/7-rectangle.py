#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """define a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initiale the rectangle"""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width instance attribute."""

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """getter of height instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height instance attribute."""

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """get area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """get perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """print # for width and height"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            for n in range(self.__height):
                for t in range(self.__width):
                    string += str(self.print_symbol)
                if (n + 1) < self.__height:
                    string += '\n'
        return string

    def __repr__(self):
        """return string by name of class and his data"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """print message {Bye rectangle...} when delet called"""
        if Rectangle.number_of_instances >= 1:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
