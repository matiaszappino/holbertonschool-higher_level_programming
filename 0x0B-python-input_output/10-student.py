#!/usr/bin/python3
"""Student"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """Init Student Class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        flag = 0
        new_dict = {}

        if type(attrs) is list:
            for i in attrs:
                if type(i) != str:
                    return self.__dict__
            for i in attrs:
                if i not in new_dict and i not in self.__dict__:
                    new_dict[i] = 
            return self.__dict__