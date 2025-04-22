import MyLinkedList


class MyListPriorityQueue:
    def __init__(self):
        # TODO

        self.list = MyLinkedList.MyLinkedList()


    def get_size(self):
        """returns the number of elements in the PQ
        @return number of elements
        """
        # TODO
        returned_size = self.list.get_size()
        return returned_size

    def is_empty(self):
        """determines if the PQ is empty or not
        @return True or False
        """
        sized = self.list.get_size()
        if sized == 0:
            return True
        else:
            return False


    def insert(self, element):
        """creates a node including the given element and adds it in the PQ
        @param element: the element to be added
        @raises ValueError if element is None # Is done automatically because this was topic of the
        # method add_sorted in the implemented function
        """
        # TODO
        self.list.add_sorted(element)
        return

    def remove_min(self):
        """returns and removes the node containing the minimum element from the PQ
        @return the element from the node that has been removed or None if the element was not found
        """
        # TODO
        # the implemented class MyLinkedList already delivers an increasingly sorted list --> first
        # element is the smallest. --> remove_first method from implemented class
        if self.list.head == None:
            return None
        else:
            return self.list.remove_first()


    def get_min(self):
        """Returns the minimum element of the PQ without removing the node containing it
        @return the minimum element of the PQ or None if the element was not found
        """
        # TODO
        if self.list.head == None:
            return None
        else:
            return self.list.get_first()

    def to_list(self):
        """Returns a list representation of the PQ
        @return a list
        """
        # TODO
        return self.list.to_list()

    def to_string(self):
        """Returns a string representation of the PQ
        @return a string
        """
        # TODO
        return self.list.to_string()


