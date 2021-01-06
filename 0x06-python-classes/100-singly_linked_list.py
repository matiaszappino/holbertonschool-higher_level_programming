#!/usr/bin/python3


class Node:
    """class of node"""

    def __init__(self):
        """Def Init"""
        self.__data = 0
        self.__next_node = None

    @property
    def data(self):
        """Data"""
        return self.__data

    @property
    def next_node(self):
        """next node"""
        return self.__next_node

    @data.setter
    def data(self, value):
        """Def Data"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """Def next node"""
        if type(value) != Node and type(value) is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Single linked list"""

    def __init__(self):
        """Def Init"""
        self.__head = None

    def __str__(self):
        """Def str"""
        current = self.head
        while(current):
            print(current.data)
            current = current.next_node
        return " "

    def sorted_insert(self, value):
        """Def Sorted List"""
        newNode = Node()
        newNode.data = value
        newNode.next_node = None
        if self.__head is not None:
            current = self.head
            while(current.next_node):
                current = current.next_node
            current.next_node = newNode
        else:
            self.head = newNode
