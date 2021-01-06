#!/usr/bin/python3
"""Magic module"""

import math


class MagicClass:
    """Magic Class"""
    def __init__(self, radius=0):
        """Constructor method"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """return the area of a circle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """retutrn a circumference of a circle"""
        return (2 * math.pi * self.__radius)
