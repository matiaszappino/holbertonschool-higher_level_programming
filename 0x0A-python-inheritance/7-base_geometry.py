#!/usr/bin/python3
"""Base Geometry"""


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")


class BaseGeometry:
    """Empty class BaseGeometry"""
    pass

    def area(self):
        """Raises an Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise TypeError('{} must be greater than 0'.format(name))
        if type(name) is not str:
            raise TypeError('name must be a string'.format(name))
    
