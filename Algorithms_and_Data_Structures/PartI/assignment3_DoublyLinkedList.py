from My_ListNode import My_ListNode

class My_DoublyLinkedList:

    """A base class providing a doubly linked list representation."""

    """/***********************************************************
	* DON'T TOUCH THIS CODE
	* Methods for testing your code after submission.
	***********************************************************/"""

    _myList_head = None
    _myList_tail = None
    _myList_size = 0

    def __init__(self,new_head=None,new_tail=None,new_size=0):
        """Create a list and default values are None."""
        self._header = new_head
        self._tail = new_tail
        self._size = new_size

    def _len_(self):
        """Return the number of elements in the list."""
        return self._size

    def list_is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def _get_header(self):
        return  self._header

    def _get_tail(self):
        return  self._tail

    """/***********************************************************
	***********************************************************/"""

# For this single task I needed 16 hours. In my point of view, it was a very difficult topic without explanations
# from the lecture.

    def insert_ordered(self, integer_val):
        new_node_one = My_ListNode(data=integer_val)
        new_node = new_node_one.data

        try:
            int(integer_val)
        except ValueError:
            print('Value Error: The input couldn\'t be transformed to an integer')

        if self._header is None: # The list is empty
            #new_node.pre_val = None
            self._header = new_node
            self._tail = new_node
            new_node_one.prev_val = new_node # So there is no overlapping with the next incoming integer


        elif self._header > new_node:
            new_node_one.prev_val = new_node   # No overlapping with the next integer_value for new_node # None?????
            new_node_one.next_val = self._header # Unkown variable = known variable
            self._header = new_node

        elif self._tail < new_node:
            tail = self._tail
            new_node_one._set_prev_val(tail)
            new_node_one._get_prev_val()
            #new_node_one.prev_val = self._tail # The second way of doing what was in the two lines before
            new_node_one.next_val = new_node # The new_node also become the next_value, so the algorithm can work without None here
            self._tail = new_node
            return next == new_node_one.next_val

        elif new_node_one.prev_val < new_node and new_node_one.next_val >= new_node:
            new_node_one.prev_val.next_val = new_node
            new_node.prev_val = new_node_one.prev_val
            new_node_one.next_val.prev_val = new_node
            new_node.next_val = new_node_one.next_val

        self._size += 1

    def _remove_(self, integer_val):
        head = self._header
        new_node_one = My_ListNode(head)
        new_node = new_node_one.data

        try:
            int(integer_val)
        except ValueError:
            print('Value Error: The input couldn\'t be transformed to an integer')

        if int(integer_val) is new_node:
            return True
        else:
            return False

        if new_node_one.prev_val is None:
            self._header = new_node_one.next_val
            self._size -= 1
        else:
            new_node_one.prev_val.next_val = new_node_one.next_val
            self._size -= 1

        if new_node.next_val is None:
            self._tail = new_node.prev_val
            if not new_node_one.prev_val is None:
                self._size -= 1
        else:
            new_node_one.next_val.prev_val = new_node_one.prev_val

    def remove_duplicates(self):
        new_node_one = My_ListNode()
        new_node = new_node_one.data

        if new_node == new_node_one.next_val:
            if new_node_one.prev_val.prev_val is None:
                new_node_one.next_val.next_val = self._header

            if new_node_one.next_val.next_val is None:
                new_node_one.prev_val.prev_val = self._tail

            new_node_one.prev_val.prev_val.next_val = new_node_one.next_val.next_val
            new_node_one.next_val.next_val.prev_val = new_node_one.prev_val.prev_val

            self._size -= 2

    def reorder_list(self):
        head = self._header
        current_val_one = My_ListNode(head)
        current_val = current_val_one.data

        if current_val % 2 != 0: # If all list elements are odd return -1
            return -1

        for current_val in range(self._size):
            if current_val is None:
                raise ValueError('Value Error: Index is out of range!')
            if current_val % 2 != 0:
                current_val = current_val_one.prev_val # All odd numbers are sorted at the first part of the list
                current_odd = current_val
                for i_odd in current_odd: # sort within the odd numbers after their amount
                    if i_odd > current_odd:
                        current_odd.prev_val = i_odd.prev_val
                        current_odd.next_val = i_odd
                        i_odd = current_odd.next_val
                        i_odd.next_val = current_odd.next_val.next_val
            else: # same pattern for even numbers
                current_val = current_val_one.next_val
                current_even = current_val
                for i_even in current_even:
                    if i_even > current_even:
                        current_even.prev_val = i_even.prev_val
                        current_even.next_val = i_even
                        i_even = current_even.next_val
                        i_even.next_val = current_even.next_val.next_val

        for i in range(self._size): # range starts with zero as the index
            if current_val % 2 == 0:
                return i # This is the index of the first even number in the list
                break
            current_val = current_val.next

        if current_val % 2 != 0: # If all list elements are odd return -1
            return -1

    def get_integer_value(self, index):
        head = self._header
        current_val_one = My_ListNode(head)
        current_val = current_val_one.data

        for i in range(int(index)):
            if current_val is None:
                raise ValueError('Value Error: Index is out of range!')

            elif i == int(index):
                return current_val # return the value with the index that was typed in

            current_val = current_val_one.next # go to the next element

