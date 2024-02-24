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

    def area(self):
        """get area of reactangle"""
        return self.__width * self.__height

    def display(self):
        """display character # by width and height"""
        for r in range(self.__y):
            print()
        for t in range(self.__height):
            for s in range(self.__x):
                print(" ", end="")
            for i in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args):
        """add args from tuple to each argument"""
        for arg in range(len(args)):
            """
            if args[0]:
                super().__init__(args[0])
            if args[1]:
                self.check_value("width", args[1])
                self.__width = args[1]
            if args[2]:
                self.check_value("height", args[2])
                self.__height = args[2]
            if args[3]:
                self.check_value("x", args[3], False)
                self.__x = args[3]
            if args[4]:
                self.check_value("y", args[4], False)
                self.__y = args[4]"""

            switcher = {
                    0: super().__init__(args[0]),
                    1: self.__width = (args[1]),
                    2: self.__height = (args[2]),
                    3: self.__x = (args[3]),
                    4: self.__y = (args[4]),
                    }
    def check_value(self, name, value, not_zero = True):
        """check if value is number integer bigger than 0 or equal"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0 and not_zero:
            raise ValueError("{} must be > 0".format(name))
        elif value <= 0 and not_zero == False:
            raise ValueError("{} must be >= 0".format(name))

    def __str__(self):
        """destractor of reactangle class"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
            self.__x, self.__y, self.__width, self.__height))
