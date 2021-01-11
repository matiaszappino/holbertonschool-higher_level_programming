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

    def area(self):
        """Returns the Rectangle Area"""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Returns the Rectangle Perimeter"""
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = (self.__width * 2) + (self.__height * 2)
        return perimeter

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