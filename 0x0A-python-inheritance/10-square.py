#!/usr/bin/python3
"""Base Geometry"""


class BaseGeometry:
    """Empty class BaseGeometry"""

    def area(self):
        """Raises an Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise TypeError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    def __init__(self, width, height):
        """Init"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area Method"""
        return (self.__width * self.__height)

    def __str__(self):
        """Str method"""
        return "[Rectangle] {}/{}>".format(self.__width, self.__height)


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
