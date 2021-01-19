#!/usr/bin/python3
"""Printed Sorted"""

if __name__ == "__main__":
    """Test cases"""
    import doctest
    doctest.testfile("tests/1-my_list.txt")


class MyList(list):
    """Class Mylist"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
