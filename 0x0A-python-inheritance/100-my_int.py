#!/usr/bin/python3
"""My Int"""


class MyInt(int):
    """Class MyInt"""
    def __init__(self, number):
        """Init MyInt"""
        self.__number = number

    def __eq__(self, number):
        """compare object if is equal than"""
        return self.__number != self.__number

    def __ne__(self, Square):
        """compare object if is not equal than"""
        return self.__number == self.__number
