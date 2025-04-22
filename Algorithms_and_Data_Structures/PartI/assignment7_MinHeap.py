class MinHeap:
    def __init__(self, list):
        """
        @param list from which the heap should be created
        @raises ValueError if list is None.
        Creates a bottom up min heap in place.
        """
        self.new = False # will become true when the searched value is contained in heap

        self.heap = list
        self.size_heap = len(list)
        # TODO
        if list == None:
            raise ValueError('List is None!')
        else:

            for iterations in range((int(len(self.heap)/2))+1): # e. g. we have a parent-child-relation of 10-7-4-1:
                # when the one goes upwards the four comes at its place, however, this place is never visited again
                # without this for-loop even though the 4 is smaller than the 7
                index = len(self.heap) - 1
                for ele in self.heap[::-1]: # go backwards through heap
                    current_ele = self.heap[index]
                    parent_index = int((index-1)/2)
                    try:
                        parent_ele = self.heap[parent_index]
                        if parent_ele > ele: # then switch them
                            self.heap[parent_index] = current_ele
                            self.heap[index] = parent_ele
                    except:
                        pass
                    index -= 1

    def get_heap(self):
        # helper function for testing, do not change
        return self.heap

    def get_size(self):
        """
        @return size of the min heap
        """
        return self.size_heap

    def contains(self, val):
        """
        @param val to check if it is contained in the min heap
        @return True if val is contained in the heap else False
        @raises ValueError if val is None.
        Tests if an item (val) is contained in the heap. Do not search the entire array sequentially, but use the properties of a heap
        """
        if val == None:
            raise ValueError('Have a look at method "contains": A None-value was putted in.')
        else:
            self.help_contains(val, self.heap[0], 0)
            t = self.new
            if t == None:
                t = False
            self.new = None # becomes None again to use it when another values are searched
            return t

    def help_contains(self, val, compare_ele, compare_ind):
        left_child_ind = int((compare_ind * 2) + 1)
        right_child_ind = int((compare_ind * 2) + 2)



        if val == compare_ele:
            self.new = True # it only changes it status from None to True when the values was found
            return self.new

        elif val > compare_ele:
            if left_child_ind < len(self.heap) and right_child_ind < len(self.heap):
                left_child = self.heap[left_child_ind]
                right_child = self.heap[right_child_ind]
                self.help_contains(val, left_child, left_child_ind)
                return self.help_contains(val, right_child, right_child_ind)

            elif left_child_ind < len(self.heap):
                left_child = self.heap[left_child_ind]
                return self.help_contains(val, left_child, left_child_ind)

            elif right_child_ind < len(self.heap):
                right_child = self.heap[right_child_ind]
                return self.help_contains(val, right_child, right_child_ind)
            else: # the comparison element has no children
                return  # is always returned when value was not found in heap

        else: # compare element is smaller than searched value
            return

        if compare_ind == len(self.heap)-1:
            return


    def is_empty(self):
        """
        @return True if the heap is empty, False otherwise
        """
        if self.size_heap == 0:
            return True

        else:
            return False

    def remove_min(self):
        """
        Removes and returns the minimum element of the heap
        @return minimum element of the heap or None if heap is empty
        """

        if len(self.heap) == 0:
            return None

        elif len(self.heap) == 1:
            min_element = self.heap[0]
            self.heap = []
            self.size_heap = 0
            return min_element

        else:
            self.size_heap -= 1
            # when the root should be replaced use the last element in the list because it is the last
            # node in the heap:
            min_element = self.heap[0]

            last_element = self.heap[-1]

            self.heap[0] = last_element # root element is replaced by the last element
            self.heap = self.heap[:-1] # cut the last not needed element away from list
            # the last element is now the first one --> Downheap now:
            return self.downheap(1, min_element) # index 1 stands in this(!) case for first element in list

    def downheap(self, index, min_element):
        wanderer_element = self.heap[index - 1] # -1 because index starts with 1 instead of 0
        try:
            left_child_element = self.heap[index*2 - 1]

            if left_child_element < wanderer_element:
                self.heap[index*2-1] = wanderer_element
                self.heap[index-1] = left_child_element

                return self.downheap(index*2, min_element)

            else: # left child isn't smaller than wanderer_element
                try: # try the right child (there exists a left child)
                    right_child_element = self.heap[index * 2 + 1 - 1]

                    if right_child_element < wanderer_element:
                        self.heap[index * 2 + 1 - 1] = wanderer_element
                        self.heap[index - 1] = right_child_element

                        return self.downheap(index * 2 + 1, min_element)
                    else: # Neither the right child nor the left child are smaller than the wanderer_element
                        return min_element

                except: # there is no right child and the left child isn't smaller than the wanderer_element
                    return min_element

        except: # there is no left child so try if there is a right child
            try: # try the right child (there exists NO left child)
                right_child_element = self.heap[index * 2 + 1 - 1]

                if right_child_element < wanderer_element:
                    self.heap[index * 2 + 1 - 1] = wanderer_element
                    self.heap[index - 1] = right_child_element
                    return self.downheap(index * 2 + 1, min_element)
                else:
                    return min_element

            except: # There aren't any children
                return min_element

    def sort(self):
        """
        @return the sorted (descending) list, e.g. [8,7,5,3,2,1]
        This method sorts the list in-place.
        """
        if self.size_heap == 1:
            self.size_heap = 0
            return self.heap # last element of heap is also the minimum of heap which should be placed at the same position
            # --> list is already finished


        # take the root of the heap and store it in variable:
        temporary_storage = self.heap[0]
        last_element = self.heap[self.size_heap-1]
        self.size_heap -= 1
        self.heap[0] = last_element


        # downheap to get new smaller valid heap:
        self.downheap_onlyinheap(0, self.heap[0])

        # put in the removed minimum at the end of the heap:

        self.heap[self.size_heap -1 + 1] = temporary_storage # -1 because we need index, + 1 because we want to be at the
        # first position outside the heap (in the list)

        # repeat this procedure until we have a sorted list:
        return self.sort()


    def downheap_onlyinheap(self, index, current_element): # down heap until the end of heap and NOT the end of list
        left_child_index = int(index * 2 + 1)
        right_child_index = int(index * 2 +2)

        if left_child_index < self.size_heap: # then you can downheap
            left_child = self.heap[left_child_index]
            current_element = self.heap[index]
            if current_element > self.heap[left_child_index]:
                self.heap[index] = left_child
                self.heap[left_child_index] = current_element
                return self.downheap_onlyinheap(left_child_index, left_child)
            elif right_child_index < self.size_heap and current_element > self.heap[right_child_index]:
                right_child = self.heap[right_child_index]
                self.heap[index] = right_child
                self.heap[right_child_index] = current_element
                return self.downheap_onlyinheap(right_child_index, right_child)

        else: # do nothing when the children are outside the heap (not necessary outside the list)
            return

