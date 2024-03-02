#!/usr/bin/python3
"""class module."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square class inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """constractor of square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter and setter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of size value"""
        #self.check_value("width", value)
        self.width = self.height = value

    def __set_update(self, id=None, size=None, x=None, y=None):
        """set update in square class"""

        if id:
            self.id = id

        if size:
            self.width = self.height = size

        if x:
            self.x = x

        if y:
            self.y = y

    def update(self, *args, **kwargs):
        """update argument in square class"""
        if args:
            self.__set_update(*args)

        elif kwargs:
            self.__set_update(**kwargs)

    def to_dictionary(self):
        """convart data of square to dictionary"""
        return {"id": self.id, "x": self.x, "size": self.width, "y": self.y}

    def __str__(self):
        """destractor of square class"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))
