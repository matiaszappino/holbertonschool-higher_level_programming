#!/usr/bin/python3
"""Acces and update private atribute"""


class Square:
    """Square Class"""
    pass

    def __init__(self, size=0, position=(0, 0)):
        """Def Init Size and Position"""
        self.__size = size
        self.__position = position

    def area(self):
        """Def Area"""
        area = self.__size * self.__size
        return area

    def my_print(self):
        """My print"""
        if self.__size == 0:
            print()
        for h in range(self.__position[1]):
                print("\n", end="")
        for i in range(0, self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
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

    @property
    def position(self):
        """Return Position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position of the Square"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
