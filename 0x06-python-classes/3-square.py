#!/usr/bin/python3
"""Area of a Square"""
class Square:
"""Square Class"""
    pass

    def __init__(self, size=0):
    """Def Init Size"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
    """Def Area"""
        area = self.__size * self.__size
        return area
