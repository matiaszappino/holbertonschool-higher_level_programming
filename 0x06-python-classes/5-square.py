#!/usr/bin/python3
"""Acces and update private atribute"""


class Square:
    """Square Class"""
    pass

    def __init__(self, size=0):
        """Def Init Size"""
        self.__size = size

    def area(self):
        """Def Area"""
        area = self.__size * self.__size
        return area

    def my_print(self):
        """My print"""
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__size):
                print("#", end="")
            print()

    @property
    def size(self):
        """Return Size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size of the Square"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
