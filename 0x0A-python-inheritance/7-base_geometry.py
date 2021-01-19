#!/usr/bin/python3
"""Base Geometry"""


if __name__ == "__main__":
    """Test cases"""
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")


class BaseGeometry:
    """Empty class BaseGeometry"""
    pass

    def area(self):
        """raises an Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
