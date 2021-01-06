#!/usr/bin/python3

class Node:
    """class of node"""

    def __init__(self):
        self.__data = 0
        self.__next_node = None

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if type(value) != Node and type(value) != None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Single linked list"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next_node
        return " "

    def sorted_insert(self, value):
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

