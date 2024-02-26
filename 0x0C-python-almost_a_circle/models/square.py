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
        self.check_value("width", value)
        self.width = self.height = value

    def __str__(self):
        """destractor of square class"""
        return("[Square] ({}) {}/{} - {}".format(self.id,
            self.x, self.y, self.width))
