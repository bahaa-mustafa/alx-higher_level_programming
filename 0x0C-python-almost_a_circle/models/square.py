#!/usr/bin/python3
"""class module."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square class inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """constractor of square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """destractor of square class"""
        return("[Square] ({}) {}/{} - {}".format(self.id,
            self.x, self.y, self.width))
