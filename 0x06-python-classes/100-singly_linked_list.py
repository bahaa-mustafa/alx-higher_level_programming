#!/usr/bin/python3
"""Node modual."""


class Node:
    """Define node."""
    def __init__(self, data, next_node=None):
        """Constractor.

        Args:
            data: data of node
            next_node: poin to next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter and setter.

        Raise:
            TypeError: when data is not integer

        Return: data
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """get and set for next_node.

        Raise:
            TypeError: when it is not none or not node

        Return: next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (not isinstance(value, Node) and
                value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """define a class."""
    def __init__(self):
        """set head of node"""
        self.__head = None

    def sorted_insert(self, value):
        """set new node.
        insert new node according to data order in 
        three cases if node is empty or has a data
        and it big than our data and in case it less than
        our data.

        Args:
            value: intger value
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node

        elif self.__head.data > value:
            new_node.next_node = self.__head
            self._head = new_node

        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node

            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """define the print function.
        it is like a constractor function and
        it called when called print

        Return: linked list each sdata in new line"""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))

