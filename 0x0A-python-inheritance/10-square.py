#!/usr/bin/python3
"""Base Geometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size):
        """Init with size"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area Method"""
        return super().area()

    def __str__(self):
        """Str method"""
        return super().__str__()
