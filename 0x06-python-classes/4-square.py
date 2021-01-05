#!/usr/bin/python3
"""Acces and update private atribute"""
class Square:
"""Square Class"""
    pass

    def __init__(self, size=0):
    """Def Init Size"""
        #if type(size) != int:
         #   raise TypeError('size must be an integer')
        #if size < 0:
         #   raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
    """Def Area"""
        area = self.__size * self.__size
        return area

    @property
    """Property"""
    def size(self):
        return self.__size

    @size.setter
    """Size of the square"""
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
