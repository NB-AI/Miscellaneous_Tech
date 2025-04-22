class MyHeapPriorityQueue:
    def __init__(self, init_capicity):
        """@param init_capacity: the initial capacity of the min heap
        """
        # inital capacity: every time by adding new element to full array double size of array; it is the
        # size
        heap_list = []
        for i in range(init_capicity):
            heap_list.append(None)

        self.heap = heap_list
        self.size = 0

        self.capa = init_capicity
        self.root = None


    def get_heap(self):
        """for testing purposes only
        """
        return self.heap

    def insert(self, element):
        """inserts an element in the min heap
        @param element: the element to be inserted
        @raises ValueError if element is None
        """
        # TODO
        if element == None:
            raise ValueError('The inserted element is None!')
        elif self.heap == []:
            self.root = element
            self.size += 1
            self.heap = [element]
            return
        else:

            if None not in self.heap: # the heap is full and has to be expanded
                heap_length_new = 2*len(self.heap)#+1 # +1 because we start with a single node/root with two possible children
                heap_length_old = len(self.heap)
                heap_length_difference = heap_length_new - heap_length_old
                for i in range(heap_length_difference):
                    self.heap.append(None)

            index = 0
            for e in self.heap:
                if e == None:
                    self.heap[index] = element
                    index_element = index
                    print(self.heap,'LO heap')
                    break
                index += 1

            self.size += 1
            self.upheap(index_element, element)

    def upheap(self, index, element):
        # compare element with its parent
        print(index)
        parent_index = int(index/2)

        try:
            self.heap[parent_index]
            parent_element = self.heap[parent_index]  # -1 because the python lists start by 0 but we
            print(parent_element, 'F')
            if element < parent_element: # then exchange them
                self.heap[index] = parent_element
                self.heap[parent_index] = element
                if parent_index > 0:
                    return self.upheap(parent_index, element)
                else:
                    return
        except:
            return

    def is_empty(self):
        """returns True if the min heap is empty, False otherwise
        @return True or False
        """
        # TODO
        counter = 0
        for i in self.heap:
            counter += 1
        if counter == 0:
            return True
        else:
            return False
        """
        if self.size == 0:
            return True
        else:
            return False"""

    def get_min(self):
        """returns the minimum element of the min heap without removing the node containing it or None if the element was not found
        @return the minimum element or None
        """
        # TODO
        if self.heap[0] == None:
            return None
        else:
            return self.heap[0]

    def remove_min(self):
        """returns the minimum element of the min heap and removes the node containing it or None if the element was not found
        @return the minimum element or None
        """
        # TODO
        # the first element in the array is the minimum and also the root
        if self.size == 0:
            return None
        elif self.size == 1:
            min_element = self.heap[0]
            self.size = 0
            self.heap = self.heap[1:]
            print(self.heap, 'here')
            return min_element
        else:
            self.size -= 1
            # when the root should be replaced use the last element in the list because it is the last
            # node in the heap:
            min_element = self.heap[0]

            downheap_list = []
            index_i = 0
            index_before = -1
            for i in self.heap:
                if i != None:
                    downheap_list.append(i) # get the last not None-element to put it at the front of self.heap few lines later
                if i == None and index_i > 0: # turn the last not None-element into a None-element
                    if self.heap[index_before] != None:
                        self.heap[index_before] = None
                index_i += 1
                index_before += 1

            self.heap[0] = downheap_list[-1] # root element is replaced by the last element
            self.heap = self.heap[:-1] # when you remove the minimum the array becomes smaller, delete one None because
                                        # the last not None-element was transformed to a None-element
            print(self.heap, 'FFFFFFFFFF')
            # the last element is now the first one --> Downheap now:
            return self.downheap(1, min_element) # index 1 stands in this(!) case for first element in list

    def downheap(self, index, min_element):
        wanderer_element = self.heap[index - 1] # -1 because index starts with 1 instead of 0
        try:
            left_child_element = self.heap[index*2 - 1]
            if left_child_element != None:
                if left_child_element < wanderer_element:
                    self.heap[index*2-1] = wanderer_element
                    self.heap[index-1] = left_child_element
                    print(self.heap, 'downheaped heap left')
                    # passt das die zwei zeilen drüber so???
                    return self.downheap(index*2, min_element)
            else: # left child isn't smaller than wanderer_element
                try: # try the right child (there exists a left child)
                    right_child_element = self.heap[index * 2 + 1 - 1]
                    if right_child_element != None:
                        # right_child_index = index*2+1
                        # print(right_child_index)
                        # right_child_element = self.heap[right_child_index-1]
                        print(right_child_element)
                        if right_child_element < wanderer_element:
                            self.heap[index * 2 + 1 - 1] = wanderer_element
                            self.heap[index - 1] = right_child_element
                            print(self.heap, 'downheaped heap right')
                            return self.downheap(index * 2 + 1, min_element)
                        else: # Neither the right child nor the left child are smaller than the wanderer_element
                            return min_element
                    else: return min_element
                except: # there is no right child and the left child isn't smaller than the wanderer_element
                    return min_element
        except: # there is no left child so try if there is a right child
            try: # try the right child (there exists NO left child)
                right_child_element = self.heap[index * 2 + 1 - 1]

                print(right_child_element)
                if right_child_element != None:
                    if right_child_element < wanderer_element:
                        self.heap[index * 2 + 1 - 1] = wanderer_element
                        self.heap[index - 1] = right_child_element
                        print(self.heap, 'downheaped heap right')
                        return self.downheap(index * 2 + 1, min_element)
                    else:
                        return min_element
                else: return min_element
            except: # There aren't any children
                print('FIN')
                return min_element

    def get_size(self):
        """returns the number of elements in the min heap
        @return element count
        """
        # TODO
        return self.size

tester = MyHeapPriorityQueue(8)

tester.insert(8)

tester.insert(9)
tester.insert(10)
tester.insert(4)

print(tester.get_heap())

print(tester.get_min())
print(tester.remove_min())
print(tester.remove_min())
print(tester.remove_min())
print(tester.get_heap())
print(tester.remove_min())
print(tester.get_size(), 'size')
print(tester.is_empty(), tester.get_heap(), 'empty')
"""


"""