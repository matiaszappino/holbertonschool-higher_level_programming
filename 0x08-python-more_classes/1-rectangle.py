#!/usr/bin/python3
"""Define a Class Rectangle"""


class Rectangle:
    """Class Rectangle"""
    def __init__(self, width=0, height=0):
        """Def Init Width and Height"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Return de Heigth of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Heigth Setter"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value