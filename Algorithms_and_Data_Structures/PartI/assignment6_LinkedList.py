import MyListNode
#from MyListNode import MyListNode


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.head = self.tail
        self.size = 0


# alles um 4 leerzeichen einrücken

    def get_head(self):
        """for testing purposes, returns the head of the linked list
        """
        return self.head

    def get_size(self):
        """returns the number of nodes in the linked list in O(1)
        """
        # TODO
        return self.size

    def add_first(self, element):
        """creates a node including the given element and adds it to the beginning of the linked list
        @param element of the new node to be added
        @raises ValueError if the element is None
        """
        # TODO
        if element == None:
            raise ValueError('Added element is None!')
        else:
            new_node = MyListNode.MyListNode(element=element) # get class from imported file
            new_node.next = self.head
            self.head = new_node

            if self.tail == None:
                self.tail = self.head

            self.size += 1
            return


    def add_last(self, element):
        """creates a node including the given element and addsit to the end of the linked list
        @param element of the new node to be added
        @raises ValueError if the element is None
        """
        # TODO
        if element == None:
            raise ValueError('Added element is None!')
        else:
            new_node = MyListNode.MyListNode(element=element)  # get class from imported file
            #new_node = MyListNode(element=element)
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
            if self.head == None:
                self.head = self.tail
            self.size += 1
            return

    def add_sorted(self, element):
        """creates a node including the given element and adds it at the correct position to the linked list sorted in ascending order
        @param element of the new node to be added
        @raises ValueError if the element is None
        """
        # TODO
        if element == None:
            raise ValueError('Added element is None!')
        else:
            new_node = MyListNode.MyListNode(element=element)  # get class from imported file
            if self.size == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = None
                self.size += 1
                return
            else:
                return self.help_add(new_node, self.head, None)

    def help_add(self, new_node, compare_node, old_node):
        if new_node.element <= compare_node.element:
            if old_node != None: # old_node is smaller then new_node and needed for old_node.next
                old_node.next = new_node
            elif old_node == None:
                self.head = new_node
            new_node.next = compare_node
            self.size += 1
            return

        else:
            if compare_node.next == None: # if the compare_node is the tail and it's smaller than the new_node
                compare_node.next = new_node
                new_node.next = None
                self.tail = new_node
                self.size += 1
                return
            else:
                old_node = compare_node
                compare_node = compare_node.next
                return self.help_add(new_node, compare_node, old_node) # move to next node to compare


    def clear(self):
        """removes all nodes from the linked list in O(1)
        """
        # TODO
        self.head = None
        self.tail = None
        self.head = self.tail
        self.size = 0
        return

    def remove_first(self):
        """returns the first element of the linked list and removes the node containing this element
        @return the element of the node that has been removed
        """
        # TODO

        removed_node = self.head

        if self.head.next:
            winner_node = self.head.next
            if winner_node.next:
                self.head.next = winner_node.next
            else:
                self.head.next = None

            self.head = winner_node
        else:
            self.head = None

        self.size -= 1
        return removed_node.element


    def get_first(self):
        """returns the first element of the linked list (without removing it)
        @return element of the first node
        """
        # TODO
        return self.head.element

    def contains(self, element):
        """returns true if a given element is in the linked list; false otherwise
        @return True or False
        @raises ValueError if the element is None
        """
        # TODO
        if element == None:
            raise ValueError('Element which should be searched for is None!')
        else:
            return self.help_contains(element, self.head)

    def help_contains(self, element, compare_node):
        if element == compare_node.element:
            return True
        else:
            if compare_node.next == None: # the end of the list is reached
                return False
            else:
                return self.help_contains(element, compare_node.next)

    def to_list(self):
        """returns a list representation of the linked list starting with the first element (index 0)
        @return a list
        """
        # TODO
        list_represent = []
        if self.head == None:
            return []
        else:
            return self.help_to_list(self.head, list_represent)

    def help_to_list(self, current_node, list_represent):
        if current_node.next != None:
            list_represent.append(current_node.element)
            return self.help_to_list(current_node.next, list_represent)
        else: # end of list reached
            list_represent.append(current_node.element)
            return list_represent

    def to_string(self):
        """returns a string representation of the linked list: "[1]-> [5]-> [8]-> [20]"
        @return a string: "[1][5][8][20]"
        """
        # TODO
        list_represent = self.to_list() # get the ready list
        final_string = ''
        for i in list_represent:
            final_string += f'[{i}]'
        return final_string

