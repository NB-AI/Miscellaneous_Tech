import time
from TreeNode import TreeNode


class MyBinarySearchTree:
    def __init__(self, root=None):
        self._root = root
        self._size = 0
        self.count_size = 1
        self.par = None
        self.found_element = None
        self.replacer_node = None
        self.ex = None
        self.remove_return = None
        self.rooter = None
        self.most_left = None
        self.height = None
        self.is_binary1 = None
        self.is_binary2 = True
        self.min_element = None
        self.complete1 = True
        self.complete2 = True
        self.found_depth = None
        self.root2 = None
        self.left_node2 = None
        self.right_node2 = None
        self.parent2 = None
        self.tree2 = None
        self.comparedtree = 0


    def insert(self, new_node):
        """@params new_node to insert.
        @return success if the insert operation was successful.
        @raises ValueError if Node is None.
        Insert the element elem into the tree and return True if it was successful.
        Elements with the same key are not allowed, in this case False is returned.
        None-elements are not allowed, in this case an exception is thrown.
        """
        if new_node is None:
            raise ValueError("Node to be inserted must not be None")
        if self.find(new_node.key): # against duplicates
            return False
        if self._root is None:
            self._root = new_node
        else:
            self._insert_helper(self._root, new_node) # compare root with new_node and so on # new_node comes from class
        self._size += 1
        return True


    def get_parent(self, key):
        """@param key
        @return key of parent.
        @raises ValueError if key is None.
        Search the parent node of a given key and return its key or None if not found.
        """
        self.par = None
        if key is None:
            raise ValueError('key is None but should have a value. Error in get_parent.')
        else:
            self.help_search(key, self._root)
            return self.par

    def is_root(self, key):
        """@params key
        @return boolean
        @raises ValueError if key is None.
        Returns True if the node of any given key is the root node, else returns False.
        """
        if key is None:
            raise ValueError('key is None but should have a value. Error in is_root.')
        else:
            if key == self._root.key:
                return True
            else:
                False

    def get_size(self):
        """@return Tree size.
        returns the number of items in the tree.
        """
        self.count_size = 1
        self.help_get_size(self._root)
        return self.count_size

    def find(self, key):
        """@params key
        @return The corresponding element of the node with the given key.
        @raises ValueError if key is None
        Returns the element of the node found with the given key, or None if element was not found.
        """
        #TODO
        self.found_element = None
        if self._root is None:
            pass
        elif key is None:
            raise ValueError('key is None but should have a value. Error in find function.')
        else:
            self.help_find(key, self._root)
            return self.found_element

    def remove(self, key):
        """@params key
        @return success of the remove operation.
        @raises ValueError if key is None.
        Removes the element with the given key, and returns True if element was found AND removed, else False.
        """
        self.remove_return = None
        if self._root is None:
            pass
        elif key is None:
            raise ValueError('key is None but should have a value. Error in remove function.')
        else:
            self.help_remove(key, self._root)
            return self.remove_return

    def is_external(self, key):
        """@params key
        @return boolean
        @raises ValueError if key is None.
        Return True if the node with the given key is an external node, otherwise return False.
        """
        self.ex = None

        if self._root is None:
            pass
        elif key is None:
            raise ValueError('key is None but should have a value. Error in is_external function.')
        else:
            self.help_is_external(key, self._root)
            return self.ex

    def is_internal(self, key):
        """@params key
        @return boolean
        @raises ValueError if key is None.
        Return True if the node with the given key is an internal node, otherwise return False.
        """
        if self._root is None:
            pass
        elif key is None:
            raise ValueError('key is None but should have a value. Error in is_external function.')
        else:
            self.is_external(key)
            if self.ex == False:
                return True
            else:
                return False

    def to_array_inorder(self, curr_node, print_array):
        """@return array
        Returns an array-representation of the stored elements (Inorder traversal).
        """
        counter_array = 0
        for i in print_array:
            counter_array += 1

        self.get_size()
        if self.count_size == counter_array:
            return print_array

        else:
            if curr_node.left_node and curr_node.left_node.element not in print_array:
                return self.help_inorder2(curr_node, print_array)

            elif curr_node.left_node == None and curr_node.right_node == None:
                #self.print_arr.append(curr_node.element)

                if curr_node.parent.left_node == curr_node and curr_node.parent.right_node and curr_node.parent.right_node.right_node == None and curr_node.parent.right_node.left_node == None:
                   # print_array.append(curr_node.parent.right_node.element)
                    #self.print_arr.append(curr_node.parent.element)
                    print_array.append(curr_node.element)
                    print_array.append(curr_node.parent.element)
                    print_array.append(curr_node.parent.right_node.element)
                    return self.to_array_inorder(curr_node.parent.parent, print_array)
                    #self.print_arr.append(curr_node.parent.right_node.element)

                elif curr_node.parent.element in print_array:
                    print_array.append(curr_node.element)
                    return self.to_array_inorder(self._root, print_array)

                else:
                    print_array.append(curr_node.element)
                    return self.to_array_inorder(curr_node.parent, print_array)
            elif curr_node.left_node and curr_node.left_node.element in print_array and curr_node.right_node == None:
                #self.print_arr.append(curr_node.element)
                print_array.append(curr_node.element)
                if curr_node.parent:
                    return self.to_array_inorder(curr_node.parent, print_array)
                else:
                    return # lasen??????
            elif curr_node.left_node and curr_node.left_node.element in print_array and curr_node.right_node.left_node:
                #self.print_arr.append(curr_node.element)
                print_array.append(curr_node.element)
                return self.help_inorder2(curr_node.right_node, print_array)
            elif curr_node.left_node and curr_node.left_node.element in print_array and curr_node.right_node and curr_node.right_node.left_node == None and curr_node.right_node.right_node == None:
                #self.print_arr.append(curr_node.element)
                print_array.append(curr_node.element)
                print_array.append(curr_node.right_node.element)
                return self.help_inorder2(self._root, print_array)
                #self.print_arr.append(curr_node.right_node.element)


            elif curr_node.left_node and curr_node.left_node.element in print_array and curr_node.right_node and curr_node.right_node.left_node == None and curr_node.right_node.right_node:
                #self.print_arr.append(curr_node.element)
                print_array.append(curr_node.element)
                return self.to_array_inorder(curr_node.right_node, print_array)
            elif curr_node.left_node == None and curr_node.right_node:
                #self.print_arr.append(curr_node.element)
                print_array.append(curr_node.element)
                return self.to_array_inorder(curr_node.right_node, print_array)



    def to_array_preorder(self, curr_node, print_array):
        """@return array
        Returns an array-representation of the stored elements (Preorder traversal).
        """
        counter_array = 0
        for i in print_array:
            counter_array += 1

        self.get_size()

        if self.count_size == (counter_array):
            return print_array

        else:
            if curr_node.left_node and curr_node.left_node.element not in print_array:
                print_array.append(curr_node.element)
                return self.to_array_preorder(curr_node.left_node, print_array)

            elif curr_node.left_node and curr_node.left_node.element in print_array and curr_node.right_node:
                return self.to_array_preorder(curr_node.right_node, print_array)

            elif curr_node.parent and curr_node.parent.element in print_array and curr_node.parent.right_node == None:
                print_array.append(curr_node.element)
                return self.help_go_up(curr_node.parent, print_array)

            elif curr_node.parent and curr_node.left_node and curr_node.right_node and curr_node.left_node in print_array and curr_node.right_node in print_array:
                return self.help_go_up(curr_node.parent, print_array)

            elif curr_node.parent and curr_node.left_node and curr_node.left_node in print_array and curr_node.right_node == None:
                return self.help_go_up(curr_node.parent, print_array)

            elif curr_node.parent and curr_node.right_node == None and curr_node.parent.right_node and curr_node.parent.right_node != curr_node and curr_node.parent.right_node.left_node == None and curr_node.parent.right_node.right_node == None:
                print_array.append(curr_node.element)
                print_array.append(curr_node.parent.right_node.element)
                return self.help_go_up(curr_node.parent, print_array)

            elif curr_node.parent and curr_node.left_node == None and curr_node.right_node == None:
                print_array.append(curr_node.element)
                return self.help_go_up(curr_node.parent, print_array)

            elif curr_node.left_node == None and curr_node.right_node:
                print_array.append(curr_node.element)
                return self.to_array_preorder(curr_node.right_node, print_array)

    def to_array_postorder(self, curr_node, print_array):
        """@return array
        Returns an array-representation of the stored elements (Postorder traversal).
        """

        counter_array = 0
        for i in print_array:
            counter_array += 1

        self.get_size()

        if self.count_size == counter_array:
            return print_array

        else:
            if curr_node.left_node and curr_node.left_node.element not in print_array:
                return self.to_array_postorder(curr_node.left_node, print_array) # go down until you end up in a left leaf
            elif curr_node.left_node == None and curr_node.right_node and curr_node.right_node.element not in print_array:
                return self.to_array_postorder(curr_node.right_node, print_array)
            elif curr_node.parent and curr_node.left_node == None and curr_node.right_node == None and curr_node.parent and curr_node.parent.left_node == curr_node and curr_node.parent.right_node == None:
                print_array.append(curr_node.element)
                return self.to_array_postorder(curr_node.parent, print_array)
            elif curr_node.parent and curr_node.left_node == None and curr_node.right_node == None and curr_node.parent and curr_node.parent.left_node == curr_node and curr_node.parent.right_node and curr_node.parent.right_node.right_node == None and curr_node.parent.right_node.left_node == None:
                print_array.append(curr_node.element)
                print_array.append(curr_node.parent.right_node.element)
                return self.to_array_postorder(curr_node.parent, print_array)
            elif curr_node.parent and curr_node.parent.right_node and curr_node.parent.right_node != curr_node:
                print_array.append(curr_node.element)
                return self.to_array_postorder(curr_node.parent.right_node, print_array)

            elif curr_node.parent and curr_node.parent.right_node == curr_node and curr_node.left_node == None and curr_node.right_node and curr_node.right_node.element not in print_array:
                return self.to_array_postorder(curr_node.right_node, print_array)

            elif curr_node.left_node == None and curr_node.right_node == None and curr_node.parent and curr_node.parent.right_node == curr_node:
                print_array.append(curr_node.element)
                return self.to_array_postorder(curr_node.parent, print_array)

            elif curr_node.right_node and curr_node.right_node.element in print_array:
                print_array.append(curr_node.element)
                return self.to_array_postorder(curr_node.parent, print_array)
            elif curr_node.left_node and curr_node.left_node.element in print_array and curr_node.right_node == None:
                print_array.append(curr_node.element)
                if curr_node.parent:
                    return self.to_array_postorder(curr_node.parent, print_array)
                else:
                    return self.to_array_postorder(curr_node, print_array)


    def is_bst(self, tree):
        """@params tree is an instance of binary search tree.
        @return True if the given tree is a binary search tree, else False.
        @raises ValueError if the tree is empty or None.
        This method verifies a given BianryTree, if it is a correct Binary Search Tree.
        """
        self.is_binary1 = None
        self.is_binary2 = True
        if tree == None:
            raise ValueError('Tree is of type None!')
        tree.get_size()

        if tree.count_size == 0:
            raise ValueError('Tree is empty!')

        if tree._root == None:
            pass
        else:
            tree.help_bst(tree, tree._root, [], [])
            tree.help_bst2(tree, tree._root)
            if tree.is_binary1 and tree.is_binary2:
                return True
            else:
                return False

    def return_min_key(self):
        """@return element of the minium key.
        Searches and returns the element of the smallest key in the bst.
        """
        self.get_size()
        if self.count_size == 0:
            return None
        else:
            self.help_min_key(self._root)
            return self.min_element

    def runtime_comparison(self, linear_list, key):
        """Creates a binary search tree abased on the given (linear) list and then determines runtime and number
        of comparisons needed to search a key in both, the internal BST and in the list. The time needed for the
        search in list and BST shall be printed on the terminal, the number of comparisons needed shall be returned
        in an array (index 0 = BST, index 1 = list)
        @param list
        @param key The key to be search in list and BST.
        @return The number of comparisons needed to find the given key in the BST.
        @raises ValueError if one of the parameters is None."""

        import datetime
        if linear_list == None:
            raise ValueError('Input key of function list is None!')
        elif key == None:
            raise ValueError('Input key of function runtime_comparison is None!')
        else:
            self.tree2 = MyBinarySearchTree()
            for element in linear_list: # build up the tree
                self.tree2.insert(TreeNode(key=element, element='N')) # element is not important here


        # Count comparisons in tree and measure its time:
        start_time_bst = datetime.datetime.now()

        self.comparedtree = 0
        self.help_comparison(self.tree2._root, key, 0)

        stop_time_bst = datetime.datetime.now()
        delta_bst = start_time_bst - stop_time_bst
        time_bst = delta_bst.total_seconds()

        # Count comparisons in list and measure its time:
        start_time_list = datetime.datetime.now()

        comparisons_list = 0
        for e in linear_list:
            comparisons_list += 1
            if e == key:
                b = (self.comparedtree, comparisons_list)

        stop_time_list = datetime.datetime.now()
        delta_list = start_time_list - stop_time_list
        time_list = delta_list.total_seconds()

        # show how much faster bst was when it was:
        if time_bst < time_list:
            c= time_list/time_bst
            print(f'BST is {c}x faster than list.')
        elif time_bst > time_list:
            c= time_list/time_bst
            print(f'BST is {c}x slower than list.')
        elif time_bst == time_list:
            print('BST is as fast as list.')

        return b




    def get_depth(self, node):
        """@param node The node of which the depth should be determined.
        @return The depth of the node.
        Determines the depth of a node in the tree.
        """
        self.found_element = None
        self.help_depth(self._root, node, 0, []) # key will always stay the same but the current_node can change
        return self.found_element
    def is_tree_complete(self):
        """Analyses the tree and determines if it is complete.
        @return True if the tree is complete, False otherwise.
        """
        self.help_complete_one(self._root,[],0,[])
        self.help_complete_two(self._root)
        if self.complete1 and self.complete2:
            return True
        else:
            return False

    ''''''''''''''''''
    '''Support Functions'''
    ''''''''''''''''''

    def _insert_helper(self, cur, new_node): # first call: cur is the root, new_node is given
        if cur.key < new_node.key:
            if cur.right_node is None: # first call: root has no right node
                cur.right_node = new_node # new node shall become the right node of the current node
                new_node.parent = cur # in addition, the current node is over the new node
            else:
                self._insert_helper(cur.right_node, new_node) # recursion, try it again this time compare new node with
                # the right node
        else: # current node key > new node key --> new node has to be left of current node
            if cur.left_node is None:
                cur.left_node = new_node
                new_node.parent = cur
            else: # when there is a left node: compare the new node with left node in the next call
                self._insert_helper(cur.left_node, new_node)

    # my functions:
    def help_search(self, key, new_node):
        if key > new_node.key: # then key node has to be on the right side of node
            if new_node.right_node:
                self.help_search(key, new_node.right_node)
            else: # no right node there
                self.par = None
                return None
        elif key < new_node.key:
            if new_node.left_node:
                self.help_search(key, new_node.left_node)
            else:
                self.par = None
                return None
        elif key == self._root.key:
            self.par = None
            return None
        elif key == new_node.key:
            if new_node.parent == self._root: # When the parent is the root return None
                self.par = None
                return None
            else:
                self.par = new_node.parent.key
                return new_node.parent.key # now we know the node in the tree which has the searched key

    def help_find(self, key, new_node):

        if key > new_node.key: # then key node has to be on the right side of node
            if new_node.right_node:
                self.help_find(key, new_node.right_node)
            else: # no right node there
                self.found_element = None # element not found in the tree
        elif key < new_node.key:
            if new_node.left_node:
                self.help_find(key, new_node.left_node)
            else:
                self.found_element = None # element not found in the tree
        elif key == new_node.key:
            self.found_element = new_node.element


    def help_get_size(self, current_node):

        if current_node.left_node:
            self.help_help_left(current_node.left_node)

        if current_node.right_node:
            self.help_help_right(current_node.right_node)

    def help_help_left(self, current_node_left):
        self.count_size += 1
        self.help_get_size(current_node_left)

    def help_help_right(self, current_node_right):
        self.count_size += 1
        self.help_get_size(current_node_right)

    def help_remove(self, key, new_node):
        # find element which shall be removed:
        if key > new_node.key:  # then key node has to be on the right side of node
            if new_node.right_node:
                self.help_remove(key, new_node.right_node)
            else:  # no right node there
                self.remove_return = False

        elif key < new_node.key:
            if new_node.left_node:
                self.help_remove(key, new_node.left_node)
            else:
                self.remove_return = False

        elif key == new_node.key:

            # Case 1: Node has no child:
            # Done
            if new_node.left_node == None and new_node.right_node == None: # ????????!!!!! or if not

                if new_node.parent.right_node == new_node:
                    new_node.parent.right_node = None
                    new_node = None
                    self.remove_return = True
                elif new_node.parent.left_node == new_node:
                    new_node.parent.left_node = None
                    new_node = None
                    self.remove_return = True

            # Case 2: Node has one child:
            # Done (one part with example)
            if new_node.right_node == None and new_node.left_node:
                if new_node.parent.left_node == new_node:
                    new_node.parent.left_node = new_node.left_node
                elif new_node.parent.right_node == new_node:
                    new_node.parent.right_node = new_node.left_node
                new_node.left_node.parent = new_node.parent

                if new_node.left_node.left_node and new_node.left_node.right_node == None:
                    new_node.left_node = new_node.left_node.left_node
                    new_node = new_node.left_node
                elif new_node.left_node.left_node == None and new_node.left_node.right_node == None:
                    new_node = new_node.left_node
                    new_node.left_node = None
                elif new_node.left_node.left_node and new_node.left_node.right_node:
                    new_node.left_node = new_node.left_node.left_node
                    new_node.right_node = new_node.left_node.right_node
                    new_node = new_node.left_node
                elif new_node.left_node.left_node == None and new_node.left_node.right_node:
                    new_node.right_node = new_node.left_node.right_node
                    new_node = new_node.left_node
                    new_node.left_node = None
                self.remove_return = True

            elif new_node.left_node == None and new_node.right_node:
                if new_node.parent.left_node == new_node:
                    new_node.parent.left_node = new_node.right_node
                elif new_node.parent.right_node == new_node:
                    new_node.parent.right_node = new_node.right_node

                new_node.right_node.parent = new_node.parent

                if new_node.right_node.left_node and new_node.right_node.right_node == None:
                    new_node.left_node = new_node.right_node.left_node
                    new_node = new_node.right_node
                    new_node.right_node = None
                elif new_node.right_node.left_node == None and new_node.right_node.right_node == None:
                    new_node = new_node.right_node
                    new_node.right_node = None

                elif new_node.right_node.left_node and new_node.right_node.right_node:
                    new_node.left_node = new_node.right_node.left_node
                    new_node.right_node = new_node.right_node.right_node
                    new_node = new_node.right_node
                elif new_node.right_node.left_node == None and new_node.right_node.right_node:
                    new_node.right_node = new_node.right_node.right_node
                    new_node = new_node.right_node

                self.remove_return = True

            # Case 3 part 1:
            # Child of current node has no children:

            elif new_node.left_node.left_node == None and new_node.left_node.right_node == None: # Left child has no children
                # Done with example
                new_node.left_node.parent = new_node.parent
                if new_node.parent.right_node == new_node:
                    new_node.parent.right_node = new_node.left_node
                elif new_node.parent.left_node == new_node:
                    new_node.parent.left_node = new_node.left_node
                new_node.right_node.parent = new_node.left_node
                new_node.left_node.right_node = new_node.right_node
                new_node = new_node.left_node
                self.remove_return = True

            elif new_node.right_node.left_node == None and new_node.right_node.right_node == None: # Right child has no children
                # Done
                new_node.right_node.parent = new_node.parent
                if new_node.parent.right_node == new_node:
                    new_node.parent.right_node = new_node.right_node
                elif new_node.parent.left_node == new_node:
                    new_node.parent.left_node = new_node.right_node
                new_node.left_node.parent = new_node.right_node
                new_node.right_node.left_node = new_node.left_node
                new_node = new_node.right_node
                self.remove_return = True

            # Case 3 part 2:
            # When children have children take the last left child of the right side:
            elif new_node.left_node.left_node or new_node.left_node.right_node:
                # right child has only one right child:
                if new_node.right_node.left_node == None and new_node.right_node.right_node:
                    new_node.right_node.left_node = new_node.left_node
                    new_node.left_node.parent = new_node.right_node

                    if new_node.parent.right_node == new_node:
                        new_node.parent.right_node = new_node.right_node

                    elif new_node.parent.left_node == new_node:
                        new_node.parent.left_node = new_node.right_node
                    new_node.right_node.parent = new_node.parent
                    self.remove_return = True
                # right child has left child
                elif new_node.right_node.left_node:
                    # Done with example, replacer deleted from old location

                    self.replacer_node = None
                    self.help_help_remove(new_node.right_node.left_node)

                    # Delete replacer_node from its old location
                    self.replacer_node.parent.left_node = None
                    self.replacer_node.parent = None

                    if self.replacer_node.right_node:
                        self.replacer_node.right_node = self.replacer_node.parent.left_node
                    if new_node.left_node:
                        new_node.left_node.parent = self.replacer_node
                        self.replacer_node.left_node = new_node.left_node
                    self.replacer_node.right_node = new_node.right_node
                    new_node.right_node.parent = self.replacer_node

                    if new_node.parent.right_node == new_node:
                        new_node.parent.right_node = self.replacer_node
                    elif new_node.parent.left_node == new_node:
                        new_node.parent.left_node = self.replacer_node
                    self.replacer_node.parent = new_node.parent

                    new_node = self.replacer_node

                    self.remove_return = True
        else:
            self.remove_return = False

    def help_help_remove(self, new_node):
        if new_node.left_node:
            new_node = new_node.left_node
            self.help_help_remove(new_node)
        else: # node has no child anymore
            self.replacer_node = new_node # this is the node that shall take the place of the removed node

    def help_is_external(self, key, new_node):
        if key > new_node.key:  # then key node has to be on the right side of node
            if new_node.right_node:
                self.help_is_external(key, new_node.right_node)
            else:  # no right node there
                self.ex = False

        elif key < new_node.key:
            if new_node.left_node:
                self.help_is_external(key, new_node.left_node)
            else:
                self.ex = False

        elif key == new_node.key:
            # An external node has no children
            if new_node.left_node == None and new_node.right_node == None:
                self.ex = True
            else:
                self.ex = False

    def help_inorder2(self, curr_node, print_array):
        if curr_node.left_node and curr_node.left_node.element not in print_array:
            return self.help_inorder2(curr_node.left_node, print_array)
        else:
            self.most_left = curr_node
            return self.to_array_inorder(curr_node, print_array)

    def help_go_up(self, curr_node, print_array):
        counter_array = 0
        for i in print_array:
            counter_array += 1

        self.get_size()
        if self.count_size == counter_array:
            return self.to_array_preorder(curr_node, print_array)
        else:

            if curr_node.right_node and curr_node.right_node.element not in print_array:
                return self.to_array_preorder(curr_node.right_node, print_array)

            elif curr_node.parent.right_node and curr_node.parent.right_node.right_node == None and curr_node.parent.right_node.left_node == None:
                print_array.append(curr_node.parent.right_node.element)
                return self.help_go_up(curr_node.parent, print_array)

            elif curr_node.parent.right_node == None:
                return self.help_go_up(curr_node.parent, print_array)

            elif curr_node.parent.right_node and curr_node.parent.right_node.left_node:
                print_array.append(curr_node.parent.right_node.element)
                return self.to_array_preorder(curr_node.parent.right_node.left_node, print_array)

            elif curr_node.parent.right_node.right_node:
                print_array.append(curr_node.parent.right_node.element)
                return self.to_array_preorder(curr_node.parent.right_node, print_array)

            elif curr_node == self._root and curr_node.right_node and curr_node.left_node and curr_node.left_node.element in print_array and curr_node.right_node.element not in print_array:
                # print_array.append(curr_node.right_node.element)
                return self.to_array_preorder(curr_node.right_node, print_array)

    def help_bst(self, tree, curr_node, par_arr, arr): # check if some parents has more than two children
        tree.get_size()
        counter_arr = 0
        for i in arr:
            counter_arr += 1

        if tree.count_size == counter_arr:
            count_par = 0
            for i in par_arr:
                count_par += 1
            for i in range(count_par):
                for j in range(i + 1, count_par):
                    for m in range(i + 2, count_par):
                        # if there is a a node which is parent of 3 nodes then this is no real binary search tree
                        if par_arr[i] == par_arr[j]:
                            if par_arr[j] == par_arr[m]:
                                tree.is_binary1 = False
                                return
                        else:
                            tree.is_binary1 = True
                            return
        else:
            if curr_node.left_node and curr_node.left_node not in par_arr:
                # go left path down
                tree.help_bst(tree, curr_node.left_node,par_arr, arr)
            elif curr_node.left_node == None and curr_node.right_node and curr_node.right_node not in par_arr:
                # go right path down
                tree.help_bst(tree, curr_node.right_node, par_arr, arr)
            elif curr_node.right_node and curr_node.left_node and curr_node.left_node in par_arr and curr_node.right_node not in par_arr:
                tree.help_bst(tree, curr_node.right_node, par_arr, arr)

            # Here are all conditions to go upwards, count parents:
            elif curr_node.left_node == None and curr_node.right_node == None:
                par_arr.append(curr_node)
                if curr_node.key not in arr:
                    arr.append(curr_node.key)
                if curr_node.parent.right_node and curr_node.parent.left_node and curr_node.parent.right_node != curr_node and curr_node.parent.left_node != curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    if curr_node.parent.left_node not in par_arr:
                        tree.left_sibling(tree, curr_node.parent.left_node, par_arr, arr)
                    if curr_node.parent.right_node not in par_arr:
                        tree.right_sibling(tree, curr_node.parent.right_node, par_arr, arr)
                    else:
                        tree.help_bst(tree, curr_node.parent, par_arr, arr)
                elif curr_node.parent.right_node and curr_node.parent.left_node and curr_node.parent.right_node == curr_node and curr_node.parent.left_node != curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    if curr_node.parent.left_node not in par_arr:
                        tree.left_sibling(tree, curr_node.parent.left_node, par_arr, arr)
                    else:
                        tree.help_bst(tree, curr_node.parent, par_arr, arr)
                elif curr_node.parent.right_node and curr_node.parent.left_node and curr_node.parent.right_node != curr_node and curr_node.parent.left_node == curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)

                    if curr_node.parent.right_node not in par_arr:
                        tree.right_sibling(tree, curr_node.parent.right_node, par_arr, arr)
                    else:
                        tree.help_bst(tree, curr_node.parent, par_arr, arr)
                elif curr_node.parent.right_node and curr_node.parent.left_node == None and curr_node.parent.right_node != curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    if curr_node.parent.right_node not in par_arr:
                        tree.right_sibling(tree, curr_node.parent.right_node, par_arr, arr)
                    else:
                        tree.help_bst(tree, curr_node.parent, par_arr, arr)
                elif curr_node.parent.left_node and curr_node.parent.right_node == None and curr_node.parent.left_node != curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    if curr_node.parent.left_node not in par_arr:
                        tree.left_sibling(tree, curr_node.parent.left_node, par_arr, arr)
                    else:
                        tree.help_bst(tree, curr_node.parent, par_arr, arr)
                else:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    tree.help_bst(tree, curr_node.parent, par_arr, arr)

            # Other part:
            elif curr_node.left_node and curr_node.right_node and curr_node.left_node in par_arr and curr_node.right_node in par_arr:
                if curr_node.parent.right_node and curr_node.parent.left_node and curr_node.parent.right_node != curr_node and curr_node.parent.left_node != curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    tree.left_sibling(tree, curr_node.parent.left_node, par_arr, arr)
                    tree.right_sibling(tree, curr_node.parent.right_node, par_arr, arr)
                elif curr_node.parent.right_node and curr_node.parent.left_node and curr_node.parent.right_node == curr_node and curr_node.parent.left_node != curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    if curr_node.parent.left_node not in par_arr:
                        tree.left_sibling(tree, curr_node.parent.left_node, par_arr, arr)
                    else:
                        tree.help_bst(tree, curr_node.parent, par_arr, arr)
                elif curr_node.parent.right_node and curr_node.parent.left_node and curr_node.parent.right_node != curr_node and curr_node.parent.left_node == curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    if curr_node.parent.left_node not in par_arr:
                        tree.right_sibling(tree, curr_node.parent.right_node, par_arr, arr)
                    else:
                        tree.help_bst(tree, curr_node.parent, par_arr, arr)
                elif curr_node.parent.right_node and curr_node.parent.left_node == None and curr_node.parent.right_node != curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    if curr_node.parent.left_node not in par_arr:
                        tree.right_sibling(tree, curr_node.parent.right_node, par_arr, arr)
                    else:
                        tree.help_bst(tree, curr_node.parent, par_arr, arr)

                elif curr_node.parent.left_node and curr_node.parent.right_node == None and curr_node.parent.left_node != curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    if curr_node.parent.left_node not in par_arr:
                        tree.left_sibling(tree, curr_node.parent.left_node, par_arr, arr)
                    else:
                        tree.help_bst(tree, curr_node.parent, par_arr, arr)

                else:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    tree.help_bst(tree, curr_node.parent, par_arr, arr)

            elif curr_node.left_node == None and curr_node.right_node and curr_node.right_node in par_arr:
                if curr_node.parent.right_node and curr_node.parent.left_node and curr_node.parent.right_node != curr_node and curr_node.parent.left_node != curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    tree.left_sibling(tree, curr_node.parent.left_node, par_arr, arr)
                    tree.right_sibling(tree, curr_node.parent.right_node, par_arr, arr)
                elif curr_node.parent.right_node and curr_node.parent.left_node and curr_node.parent.right_node == curr_node and curr_node.parent.left_node != curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    tree.left_sibling(tree, curr_node.parent.left_node, par_arr, arr)
                elif curr_node.parent.right_node and curr_node.parent.left_node and curr_node.parent.right_node != curr_node and curr_node.parent.left_node == curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    tree.right_sibling(tree, curr_node.parent.right_node, par_arr, arr)
                elif curr_node.parent.right_node and curr_node.parent.left_node == None and curr_node.parent.right_node != curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    tree.right_sibling(tree, curr_node.parent.right_node, par_arr, arr)
                elif curr_node.parent.left_node and curr_node.parent.right_node == None and curr_node.parent.left_node != curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    tree.left_sibling(tree, curr_node.parent.left_node, par_arr, arr)
                else:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    tree.help_bst(tree, curr_node.parent, par_arr, arr)

            elif curr_node.left_node and curr_node.left_node in par_arr and curr_node.right_node == None:
                if curr_node.parent.right_node and curr_node.parent.left_node and curr_node.parent.right_node != curr_node and curr_node.parent.left_node != curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    tree.left_sibling(tree, curr_node.parent.left_node, par_arr, arr)
                    tree.right_sibling(tree, curr_node.parent.right_node, par_arr, arr)
                elif curr_node.parent.right_node and curr_node.parent.left_node and curr_node.parent.right_node == curr_node and curr_node.parent.left_node != curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    tree.left_sibling(tree, curr_node.parent.left_node, par_arr, arr)
                elif curr_node.parent.right_node and curr_node.parent.left_node and curr_node.parent.right_node != curr_node and curr_node.parent.left_node == curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    tree.right_sibling(tree, curr_node.parent.right_node, par_arr, arr)
                elif curr_node.parent.right_node and curr_node.parent.left_node == None and curr_node.parent.right_node != curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    tree.right_sibling(tree, curr_node.parent.right_node, par_arr, arr)
                elif curr_node.parent.left_node and curr_node.parent.right_node == None and curr_node.parent.left_node != curr_node:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    tree.left_sibling(tree, curr_node.parent.left_node, par_arr, arr)
                else:
                    par_arr.append(curr_node.parent)
                    if curr_node.parent.key not in arr:
                        arr.append(curr_node.parent.key)
                    tree.help_bst(tree, curr_node.parent, par_arr, arr)

    def left_sibling(self, tree, curr_node, par_arr,  arr):
        tree.help_bst(tree, curr_node.parent.left_node, par_arr, arr)

    def right_sibling(self, tree, curr_node, par_arr, arr):
        tree.help_bst(tree, curr_node.parent.right_node, par_arr, arr)

    def help_bst2(self, tree, curr_node):
        if curr_node.left_node and curr_node.right_node:
            if curr_node.key < curr_node.left_node.key:
                tree.is_binary2 = False
                return
            elif curr_node.key > curr_node.right_node.key:
                tree.is_binary2 = False
                return
            else: # go to left and also to right node
                tree.help_bst2_left(tree, curr_node)
                tree.help_bst2_right(tree, curr_node)
        elif curr_node.left_node == None and curr_node.right_node:
            if curr_node.key > curr_node.right_node.key:
                tree.is_binary2 = False
                return
            else:
                tree.help_bst2_right(tree, curr_node)
        elif curr_node.left_node and curr_node.right_node == None:
            if curr_node.key < curr_node.left_node.key:
                tree.is_binary2 = False
                return
            else:
                tree.help_bst2_left(tree, curr_node)
        else: # node is a leaf
            pass

    def help_bst2_left(self, tree, curr_node):
        tree.help_bst2(tree, curr_node.left_node)
    def help_bst2_right(self, tree, curr_node):
        tree.help_bst2(tree, curr_node.right_node)

    def help_min_key(self, curr_node):
        if curr_node.left_node:
            self.help_min_key(curr_node.left_node)
        else:
            self.min_element = curr_node.element

    def help_complete_one(self, curr_node, height_arr, height, arr): # check if all leaves have the same height
        if curr_node == self._root and curr_node.left_node in arr and curr_node.right_node in arr and curr_node.left_node and curr_node.right_node:
            count_arr = 0
            for i in height_arr:
                count_arr += 1
            for i in range(count_arr):
                for j in range(i + 1, count_arr):
                    if height_arr[i] != height_arr[j]: # different heights of the leaves lead to False
                        self.complete1 = False
                        return
        if curr_node == self._root and curr_node.left_node in arr and curr_node.right_node == None and curr_node.left_node:
            count_arr = 0
            for i in height_arr:
                count_arr += 1
            for i in range(count_arr):
                for j in range(i + 1, count_arr):
                    if height_arr[i] != height_arr[j]: # different heights of the leaves lead to False
                        self.complete1 = False
                        return

        if curr_node == self._root and curr_node.left_node == None and curr_node.right_node in arr and curr_node.right_node:
            count_arr = 0
            for i in height_arr:
                count_arr += 1
            for i in range(count_arr):
                for j in range(i + 1, count_arr):
                    if height_arr[i] != height_arr[j]: # different heights of the leaves lead to False
                        self.complete1 = False
                        return


        elif curr_node.left_node and curr_node.left_node not in arr:
            height += 1
            arr.append(curr_node)
            self.help_complete_one(curr_node.left_node,height_arr, height, arr)
        elif curr_node.left_node == None and curr_node.right_node and curr_node.right_node not in arr:
            height += 1
            arr.append(curr_node)
            self.help_complete_one(curr_node.right_node, height_arr,height, arr)
        elif curr_node.left_node and curr_node.left_node in arr and curr_node.right_node and curr_node.right_node not in arr:
            height += 1
            arr.append(curr_node)
            self.help_complete_one(curr_node.right_node, height_arr,height, arr)
        elif curr_node.left_node == None and curr_node.right_node == None:
            height_arr.append(height)
            height -= 1
            arr.append(curr_node)
            self.help_complete_one(curr_node.parent,height_arr, height, arr)
        elif curr_node.left_node and curr_node.right_node and curr_node.right_node in arr and curr_node.left_node in arr:
            height -= 1
            self.help_complete_one(curr_node.parent,height_arr, height, arr)
        elif curr_node.left_node == None and curr_node.right_node and curr_node.right_node in arr:
            height -= 1
            self.help_complete_one(curr_node.parent,height_arr, height, arr)


    def help_complete_two(self, curr_node): # check if on each level is the maximum number of nodes
        if curr_node.left_node and curr_node.right_node:
            self.complete_right(curr_node.right_node)
            self.complete_left(curr_node.left_node)
        elif curr_node.left_node and curr_node.right_node == None:
            self.complete2 = False
        elif curr_node.right_node and curr_node.left_node == None:
            self.complete2 = False
        else:
            pass

    def complete_left(self, curr_node):
        self.help_complete_two(curr_node)

    def complete_right(self, curr_node):
        self.help_complete_two(curr_node)

    def help_depth(self, curr_node, node_searched, height, arr):

        if curr_node == self._root and curr_node.left_node in arr and curr_node.right_node in arr and curr_node.left_node and curr_node_right_node:
            return

        elif curr_node == self._root and curr_node.left_node in arr and curr_node.right_node==None and curr_node.left_node:
            return

        elif curr_node == self._root and curr_node.right_node in arr and curr_node.left_node==None and curr_node_right_node:
            return

        elif curr_node.key == node_searched.key:
            if curr_node.element == node_searched.element:
                self.found_element = height
                return
            else:
                return

        elif curr_node.left_node and curr_node.left_node not in arr:
            height += 1
            arr.append(curr_node)
            self.help_depth(curr_node.left_node, node_searched, height, arr)
        elif curr_node.left_node == None and curr_node.right_node and curr_node.right_node not in arr:
            height += 1
            arr.append(curr_node)
            self.help_depth(curr_node.right_node, node_searched, height, arr)
        elif curr_node.left_node and curr_node.left_node in arr and curr_node.right_node and curr_node.right_node not in arr:
            height += 1
            arr.append(curr_node)
            self.help_depth(curr_node.right_node, node_searched, height, arr)
        elif curr_node.left_node == None and curr_node.right_node == None:
            height -= 1
            arr.append(curr_node)
            self.help_depth(curr_node.parent, node_searched, height, arr)
        elif curr_node.left_node and curr_node.right_node and curr_node.right_node in arr and curr_node.left_node in arr:
            height -= 1
            self.help_depth(curr_node.parent, node_searched, height, arr)
        elif curr_node.left_node == None and curr_node.right_node and curr_node.right_node in arr:
            height -= 1
            self.help_depth(curr_node.parent, node_searched, height, arr)

    def help_comparison(self, curr_node, keyy, compared):
        if curr_node.key > keyy: # then go left
            compared +=1
            self.help_comparison(curr_node.left_node, keyy, compared)

        elif curr_node.key < keyy: # then go right
            compared +=1
            self.help_comparison(curr_node.right_node, keyy, compared)

        elif curr_node.key == keyy:
            compared += 1
            self.comparedtree = compared
            return

''''''''''''''''''
'''Test Code'''
''''''''''''''''''

test_bst = MyBinarySearchTree()
test_bst.insert(TreeNode(key=4, element="a"))
test_bst.insert(TreeNode(key=2, element="b"))
test_bst.insert(TreeNode(key=3, element="c"))
test_bst.insert(TreeNode(key=5, element="d"))
test_bst.insert(None)

print(test_bst.to_array_inorder(test_bst._root, []))
print(test_bst.to_array_preorder(test_bst._root, []))
print(test_bst.to_array_postorder(test_bst._root, []))
print(test_bst.find(1))
test_bst.remove(2)
print(test_bst.to_array_inorder(test_bst._root, []))
test_bst.remove(2)
test_bst.remove(None)
print(test_bst.is_bst(test_bst))

empty_bst = MyBinarySearchTree()
print(test_bst.is_bst(empty_bst))
