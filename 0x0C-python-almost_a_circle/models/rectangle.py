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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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

    def __set_update(self, id=None, width=None, height=None,
            x=None, y=None):
        """set arguments in ther position"""

        if id:
            super().__init__(id)

        if width:
            self.__width = width

        if height:
            self.__height = height

        if x:
            self.__x = x

        if y:
            self.__y = y

    def update(self, *args, **kwargs):
        """add args from tuple to each argument"""
        if args:
            self.__set_update(*args)

        elif kwargs:
            self.__set_update(**kwargs)

    def check_value(self, name, value, not_zero=True):
        """check if value is number integer bigger than 0 or equal"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and not_zero:
            raise ValueError("{} must be > 0".format(name))
        elif value < 0 and not not_zero:
            raise ValueError("{} must be >= 0".format(name))

    def to_dictionary(self):
        """convert rectangle data to dictionary"""
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}

    def __str__(self):
        """destractor of reactangle class"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
            self.__x, self.__y, self.__width, self.__height))
