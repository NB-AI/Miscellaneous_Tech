from avl_node import AVLNode


class AVLTree:

    def __init__(self):
        """Default constructor. Initializes the AVL tree.
        """
        self.root = None
        self.size = 0
        self.array = []
        self.restructure_list = []
        self.found_node = None
        self.replacer_parent = None
        self.max_depth = 0
        self.max_depth_list = []





    def get_root(self):
        """@returns the root of the AVLTree
        """
        return self.root

    def get_height(self):
        """Retrieves tree height.
    	 @return -1 in case of empty tree, current tree height otherwise.
    	 """
        if self.size == 0:
            return -1
        return self.root.height # root of the tree has the highest height value

    def get_size(self):
        """Yields number of key/element pairs in the tree.
        @return Number of key/element pairs.
        """
        return self.size


    def to_array(self):
        """Yields an array representation of the tree elements (pre-order).
    	@return Array representation of the tree elements.
        """
        self.array = []

        if self.root == None:
            return self.array
        self.method_preorder(self.root)

        return self.array

    def method_preorder(self, current_node):
        self.array.append(current_node.elem)


        if current_node.left and current_node.right:
            return self.method_preorder(current_node.left), self.method_preorder(current_node.right)
        elif current_node.left:
            return self.method_preorder(current_node.left)
        elif current_node.right:
            return self.method_preorder(current_node.right)
        else:
            return None

    def find(self, key):
        """Returns element of node with given key.
         @param key: Key to search.
         @return Corresponding element if key was found, None otherwise.
         @raises ValueError if the key is None
         """
        outcome = self.find2(key, None, False, self.root)
        if outcome == False:
            return None
        return outcome

    def find2(self, key, replacer_node, replace_operation, current_node):

        if key == None:
            raise ValueError('Searched key is None!')


        if current_node.key > key: # we have to go left then
            if current_node.left:
                return self.find2(key, replacer_node, replace_operation, current_node.left)

            else: # by binary tree properties there doesn't exist a node with such a key
                return False
        elif current_node.key < key: # we have to go right then
            if current_node.right:
                return self.find2(key, replacer_node, replace_operation, current_node.right)
            else:
                return False
        elif current_node.key == key: # key is found

            self.found_node = current_node
            if replace_operation == True:
                current_node.key = replacer_node.key
                current_node.elem = replacer_node.elem
                # We know delete the replacer node from its old place
                return self.go_left(starting_node=current_node, first_time=True, delete_replacer=True)

            else:

                return current_node.elem


    def insert(self, key, elem='no'):
        """Inserts a new node into AVL tree.
         @param key: Key of the new node.
         @param elem: Data of the new node. Elements with the same key
         are not allowed. In this case false is returned. None-Keys are
         not allowed. In this case an exception is thrown.
         @raises ValueError if the key or elem is None.
        """
        if key == None or elem == None:
            raise ValueError
        if elem == 'no':
            elem = key
        return self.insert2(key, elem)


    def insert2(self, key, elem):

        # When the tree is empty:
        if self.root == None:
            inserted_node = AVLNode(key, elem)
            self.root = inserted_node
            self.size += 1
            return True


        # First simply find the place for insertion:
        current_node = self.root
        finally_ = False
        marker = ''
        while finally_ == False:
            if current_node.key == key:
                return False # Because no duplicates are allowed
            elif current_node.key > key: # we have to go left then
                marker = 'left'
                if current_node.left:
                    current_node = current_node.left

                else: # the left child doesn't exist
                    finally_ = True

            elif current_node.key < key: # we have to go right then
                marker = 'right'
                if current_node.right:
                    current_node = current_node.right
                else:
                    finally_ = True

        # Now we are out of the while loop because we found a good place to insert
        inserted_node = AVLNode(key, elem)
        inserted_node.parent = current_node

        if marker == 'left':
            current_node.left = inserted_node
        elif marker == 'right':
            current_node.right = inserted_node
        self.size += 1 # number of nodes increases by 1

        # Now we have to update and check the heights of the single nodes before doing restructuring:
        # The inserted node has automatically a height of 0 because it is a leaf. (Also see beginning def structure method)
        # From this follows that the parent increases in height iff the inserted node has no sibling!:


        if inserted_node.parent.left != None and marker == 'right': # the heights don't have to be updated
            return True
        elif inserted_node.parent.right != None and marker == 'left': # inserted_node.parent.right != inserted_node: # the heights don't have to be updated

            return True
        else: # we have to update the heights:
            inserted_node.parent.height += 1
            return self.structure_method(inserted_node, True, False, False)

    def structure_method(self, inserted_node, first_call, remove_operation, heights_ready):

            stop_looping = False

            current_node2 = inserted_node.parent
            running = True
            if heights_ready == True:
                running = False
            while running == True: # we will end up with the updated heights


                # Furthermore, when we update the heights we always have to compare siblings:

                if current_node2.parent != None:
                    if current_node2.parent.left and current_node2.parent.left is not current_node2:
                        if first_call == False and current_node2.height +1 > current_node2.parent.left.height: # restructuring has also impact of remaining tree
                            current_node2.parent.height -= 1
                            if current_node2.parent != self.root:
                                current_node2 = current_node2.parent
                            else:
                                running = False
                        elif first_call == True and current_node2.height > current_node2.parent.left.height:
                            current_node2.parent.height += 1
                            if current_node2.parent != self.root:
                                current_node2 = current_node2.parent
                            else:
                                running = False
                        else: # There is no impact on the height values of the tree --> No updating needed
                                running = False

                    # same for the right siblings of the current node:
                    elif current_node2.parent.right and current_node2.parent.right is not current_node2:
                        if first_call == False and current_node2.height +1 > current_node2.parent.right.height: # restructuring has also impact of remaining tree
                            current_node2.parent.height -= 1
                            if current_node2.parent != self.root:
                                current_node2 = current_node2.parent
                            else:
                                running = False
                        elif first_call == True and current_node2.height > current_node2.parent.right.height:
                            current_node2.parent.height += 1
                            if current_node2.parent != self.root:
                                current_node2 = current_node2.parent
                            else:
                                running = False
                        else: # There is no impact on the height values of the tree --> No updating needed
                                running = False

                    else: # The current node has no siblings, so the impact is given
                        if first_call == True:
                            current_node2.parent.height += 1
                        else: # first call false # wird nicht gebraucht von stern
                            current_node2.parent.height -= 1
                        if current_node2.parent != self.root:
                            current_node2 = current_node2.parent
                        else:
                            running = False
                else:
                    running = False


            # Now all heights are updated.
            # Where is the tree not balanced anymore?
            # Start search from the inserted node:

            current_node3 = inserted_node
            x = current_node3
            balanced = True
            z, y = None, None

            mark_y = False
            while current_node3.parent and balanced == True:


                if current_node3 == self.root: # get out of the loop

                    return True # there was no inbalance found. Therefore, we are ready with inserting, height updating and restructuring

                if current_node3.parent.left and current_node3.parent.left is not current_node3:

                    if abs(current_node3.height - current_node3.parent.left.height) >= 2: # here would be an unbalanced area of the tree
                        z = current_node3.parent  # z is the inbalanced node
                        if remove_operation == True:
                            if current_node3.height >= current_node3.parent.left.height:
                                y = current_node3
                            else: # siblings height is bigger
                                y = current_node3.parent.left
                            if y.left and y.right: # y has two children from which we choose the one with the higher height
                                mark_y = True
                                if y.left.height >= y.right.height:
                                    x = y.left
                                else: # the right child has the higher height
                                    x = y.right
                            elif y.left:
                                x = y.left
                            elif y.right:
                                x = y.right
                            else:
                                print('ERROR FOUND by removing mark x,y,z!')
                        else:
                            y = current_node3
                        balanced = False
                    else:
                        x = current_node3  # the current node becomes x whereas the in the beneath the current node changes to the parent of it
                        current_node3 = current_node3.parent

                elif current_node3.parent.left == None: # Parent has only one child and thats the current node
                   if current_node3.height + 1 >= 2: # None nodes have a height of -1: node.height - (-1)
                       # By remove operation the current nodes height is smaller than before and therefore comes closer to -1 and not far away.
                       # Therefore out of interest for remove operations
                       z = current_node3.parent  # z is the inbalanced node
                       y = current_node3
                       if remove_operation == True:
                           if y.left and y.right:  # y has two children from which we choose the one with the higher height
                               mark_y = True
                               if y.left.height >= y.right.height:
                                   x = y.left
                               else:  # the right child has the higher height
                                   x = y.right
                           elif y.left:
                               x = y.left
                           elif y.right:
                               x = y.right
                           else:
                               print('ERROR FOUND by removing mark x,y,z!')
                       balanced = False
                   else:
                       x = current_node3  # the current node becomes x where as the in the beneath the current node changes to the parent of it
                       current_node3 = current_node3.parent

                elif current_node3.parent.right and current_node3.parent.right is not current_node3:
                    if abs(current_node3.height - current_node3.parent.right.height) >= 2: # here would be an unbalanced area of the tree
                        z = current_node3.parent # z is the inbalanced node
                        if remove_operation == True: # same formula again only with right
                            if current_node3.height >= current_node3.parent.right.height:
                                y = current_node3
                            else: # siblings height is bigger
                                y = current_node3.parent.right
                            if y.left and y.right: # y has two children from which we choose the one with the higher height
                                mark_y = True
                                if y.left.height >= y.right.height:
                                    x = y.left
                                else: # the right child has the higher height
                                    x = y.right
                            elif y.left:
                                x = y.left
                            elif y.right:
                                x = y.right
                            else:
                                print('ERROR FOUND by removing mark x,y,z!')
                        else:
                            y = current_node3       
                        balanced = False
                    else:
                        x = current_node3  # the current node becomes x where as the in the beneath the current node changes to the parent of it
                        current_node3 = current_node3.parent

                elif current_node3.parent.right == None:
                   if current_node3.height + 1 >= 2: # None nodes have a height of -1: node.height - (-1)
                       z = current_node3.parent  # z is the inbalanced node
                       y = current_node3
                       if y.left and y.right:  # y has two children from which we choose the one with the higher height
                           mark_y = True
                           if y.left.height >= y.right.height:
                               x = y.left
                           else:  # the right child has the higher height
                               x = y.right
                       elif y.left:
                           x = y.left
                       elif y.right:
                           x = y.right
                       else:
                           print('ERROR FOUND by removing mark x,y,z!')
                       balanced = False
                   else:
                       x = current_node3  # the current node becomes x where as the in the beneath the current node changes to the parent of it
                       current_node3 = current_node3.parent


                else: # No inbalance found
                    x = current_node3 # the current node becomes x where as the in the beneath the current node changes to the parent of it
                    current_node3 = current_node3.parent

            # If no inbalance found we are ready with inserting:

            if y == None:
                if remove_operation == True:
                    self.max_depth = 0
                    self.max_depth_list = []
                    self.array3 = []
                    # Go down whole tree and count max depth
                    self.get_max_depth(self.root, 0)

                return True




            # Now we have found the inbalanced node and marked the x,y,z-nodes
            # Next step is the restructuring of the tree.
            # We have to mark tree parts after inorder tree traversal: y is the root, x the left child of it, z the right child of it.
            # However, we have also to organize all the subtrees hanging on this three nodes:


            # Try the inorder search thorugh the tree with stopping at the children of x, y, z
            # Good to know: z don't have to be the root. So, we only restructure and search thorugh a subtree, sometimes.

            self.restructure_list = [] # We have to empty the list every time we want to restructure the tree


            self.method_inorder_sort(z,x,y,z)

            liste=[]
            for i in self.restructure_list:
                if i != None:
                    liste.append(i.key)
                else:
                    liste.append('none')

            # Now we have a list from which get the order of the new subtree
            new_small_root = self.restructure_list[3] # here is the root of the subtree

            # Connect the subtree with the big tree
            if z.parent:
                self.restructure_list[3].parent = z.parent

                if z.parent.left == z:

                    self.restructure_list[3].parent.left = self.restructure_list[3]
                elif z.parent.right == z:
                    self.restructure_list[3].parent.right = self.restructure_list[3]

            else: # z has no parent --> That means that z was the root
                self.root = self.restructure_list[3]
                self.restructure_list[3].parent = None

            if new_small_root != None:
                new_small_root.left = self.restructure_list[1]
                new_small_root.right = self.restructure_list[5]



            new_left_from_root = self.restructure_list[1]
            if new_left_from_root != None:
                new_left_from_root.parent = new_small_root
                new_left_from_root.left = self.restructure_list[0]
                new_left_from_root.right = self.restructure_list[2]

            most_left = self.restructure_list[0]
            if most_left != None:
                most_left.parent = self.restructure_list[1]

            sibling_most_left = self.restructure_list[2]
            if sibling_most_left != None:
                sibling_most_left.parent = self.restructure_list[1]



            new_right_from_root = self.restructure_list[5]
            if new_right_from_root != None:
                new_right_from_root.parent = new_small_root
                new_right_from_root.left = self.restructure_list[4]
                new_right_from_root.right = self.restructure_list[6]

            most_right = self.restructure_list[6]
            if most_right != None:
                most_right.parent = self.restructure_list[5]

            sibling_most_right = self.restructure_list[4]
            if sibling_most_right != None:
                sibling_most_right.parent = self.restructure_list[5]



            # Now the nodes of the inbalanced subtree are new ordered and connected.

            # We need to update the heights of the nodes in the modified subtree.
            if remove_operation == True:
                self.max_depth = 0
                self.max_depth_list = []
                # Go down whole tree and count max depth
                self.get_max_depth(self.root, 0)
                heights_ready = True

            else:
                heights_ready = False
                if self.restructure_list[3] == y:
                    if self.restructure_list[1] == z:
                        self.restructure_list[1].height -= 2
                    elif self.restructure_list[5] == z:
                        self.restructure_list[5].height -= 2

                elif self.restructure_list[3] ==x:
                    if self.restructure_list[1] == z:
                        self.restructure_list[1].height -= 2
                        if mark_y == False:
                            self.restructure_list[5].height -= 1 # remaining node has to y then
                    elif self.restructure_list[5] == z:
                        self.restructure_list[5].height -= 2
                        if mark_y == False:
                            self.restructure_list[1].height -= 1
                    if mark_y == True:
                        self.restructure_list[3].height += 1
                    self.restructure_list[3].height += 1

                elif self.restructure_list[3] == z:
                    if self.restructure_list[1] == y and mark_y ==False:
                        self.restructure_list[1].height -= 1

                    elif self.restructure_list[5] == y and mark_y == False:
                        self.restructure_list[5].height -= 1
                    if mark_y == False:
                        self.restructure_list[3].height -= 1


            # By this structuring process higher levels of the tree are ignored.
            # --> We have to loop over this process until
            # the root of the big tree x,y,z!


            set_ = {x,y,z}

            if self.root in set_ and remove_operation== False:
                return True
            else:
                if remove_operation == True:
                    if self.restructure_list[1].left and self.restructure_list[1].right and abs(self.restructure_list[1].left.height-self.restructure_list[1].right.height) >=2:
                        leaf = self.go_only_left(self.restructure_list[1].left)
                        return self.structure_method(leaf, False, remove_operation, heights_ready)

                    elif self.restructure_list[1].left and self.restructure_list[1].right == None and abs(self.restructure_list[1].left.height+1) >=2:
                        leaf = self.go_only_left(self.restructure_list[1].left)
                        return self.structure_method(leaf, False, remove_operation, heights_ready)

                    elif self.restructure_list[1].left == None and self.restructure_list[1].right and abs(1+self.restructure_list[1].right.height) >=2:
                        leaf = self.go_only_left(self.restructure_list[1].right)
                        return self.structure_method(leaf, False, remove_operation, heights_ready)

                    elif self.restructure_list[5].left and self.restructure_list[5].right and abs(self.restructure_list[5].left.height-self.restructure_list[5].right.height) >=2:
                        leaf = self.go_only_left(self.restructure_list[5].left)
                        return self.structure_method(leaf, False, remove_operation, heights_ready)

                    elif self.restructure_list[5].left and self.restructure_list[5].right == None and abs(self.restructure_list[5].left.height+1) >=2:
                        leaf = self.go_only_left(self.restructure_list[5].left)
                        return self.structure_method(leaf, False, remove_operation, heights_ready)

                    elif self.restructure_list[5].left == None and self.restructure_list[5].right and abs(1+self.restructure_list[5].right.height) >=2:
                        leaf = self.go_only_left(self.restructure_list[5].right)
                        return self.structure_method(leaf, False, remove_operation, heights_ready)

                    elif self.restructure_list[1].height > self.restructure_list[5].height:

                        leaf = self.go_only_left(self.restructure_list[1])
                        return self.structure_method(leaf, False, remove_operation, heights_ready)

                if self.restructure_list[1].height > self.restructure_list[5].height:
                    leaf = self.go_only_left(self.restructure_list[1])
                    return self.structure_method(leaf, False, remove_operation, heights_ready)

                else:
                    leaf = self.go_only_left(self.restructure_list[5])
                    return self.structure_method(leaf, False, remove_operation, heights_ready)

    def go_only_left(self, current_node):
        if current_node.left:
            return self.go_only_left(current_node.left)
        elif current_node.right:
            return self.go_only_left(current_node.right)
        else:
            return current_node


    def get_max_depth(self, current_node, summer):
        if current_node != self.root:
            summer += 1
        if current_node.left and current_node.right:
            return self.get_max_depth(current_node.left, summer),self.get_max_depth(current_node.right,  summer)
        elif current_node.left:
            return self.get_max_depth(current_node.left, summer)
        elif current_node.right:
            self.get_max_depth(current_node.right,  summer)
        else:
            self.max_depth_list.append(summer)
            return self.compute_max()

    def compute_max(self):
        self.max_depth = max(self.max_depth_list)
        print(self.max_depth)
        return self.actualize_final_heights(self.root, self.max_depth)

    def actualize_final_heights(self,current_node, depth):
        current_node.height = depth

        #depth -= 1
        if current_node.left and current_node.right:
            return self.actualize_final_heights(current_node.left,depth-1), self.actualize_final_heights(current_node.right,depth-1)
        elif current_node.left:
            return self.actualize_final_heights(current_node.left,depth-1)
        elif current_node.right:
            self.actualize_final_heights(current_node.right, depth-1)
        else:

            return




    def method_inorder_sort(self, current_node4, x,y,z):
        set_ = {x,y,z}
        if current_node4.left and current_node4.left in set_:
            self.method_inorder_sort(current_node4.left, x,y,z)
        elif current_node4.left and current_node4.left not in set_:
            self.restructure_list.append(current_node4.left)
        elif current_node4.left == None:
            self.restructure_list.append(None)

        self.restructure_list.append(current_node4)

        if current_node4.right and current_node4.right in set_:
            self.method_inorder_sort(current_node4.right, x,y,z)
        elif current_node4.right and current_node4.right not in set_:
            self.restructure_list.append(current_node4.right)
        elif current_node4.right == None:
            self.restructure_list.append(None)
        return



    def remove(self, key):
        """Removes node with given key.
    	 @param key: Key of node to remove.
    	 @return true If element was found and deleted.
         @raises ValueError if the key is None
        """

        if key == None:
            raise ValueError('Searched key is None!')

        self.find2(key=key, replacer_node=None, replace_operation=False, current_node=self.root) # through that we get the node to remove --> self.found_node updated
        if self.found_node == None:
           return False
        self.size -= 1
        if self.size == 0:
            self.root = None
            self.array = []
            return True

        replacer_node = self.go_left(starting_node=self.found_node, first_time=True, delete_replacer=False)
        # Lets remove the replacer node and replace the to remove node

        self.find2(key=key, replacer_node=replacer_node, replace_operation=True,
                   current_node=self.root)

        if self.replacer_parent == None:
            self.root = replacer_node
            self.to_array()
            return True
        if self.replacer_parent.parent == None:
            if replacer_node.parent.left and replacer_node.parent.left != replacer_node:
                self.structure_method(replacer_node.parent.left,False,True,False)
            elif replacer_node.parent.right and replacer_node.parent.right != replacer_node:
                self.structure_method(replacer_node.parent.right, False, True,False)
            else: # only the case when the grandparent is None and the parent of the replacer node is the root. The replacer
                # node has no children because its grandparent is None.

                return True
        else:

            if self.replacer_parent.parent.left and self.replacer_parent.parent.left != self.replacer_parent:

                if self.replacer_parent.parent.left.height < self.replacer_parent.height + 1:
                    self.replacer_parent.parent.height -= 1

            elif self.replacer_parent.parent.right and self.replacer_parent.parent.right != self.replacer_parent:
                if self.replacer_parent.parent.right.height < self.replacer_parent.height + 1:
                    self.replacer_parent.parent.height -= 1

            self.structure_method(self.replacer_parent, False, True, False)

        return True


    def go_left(self, starting_node, first_time, delete_replacer):
        if first_time == True and starting_node.right: # we try to get the most left node of the right subtree
            return self.go_left(starting_node.right, False, delete_replacer)

        elif first_time == True and starting_node.right == None and starting_node.left and delete_replacer == False:
            return starting_node.left


        if starting_node.left:
            return self.go_left(starting_node.left, False, delete_replacer)
        if delete_replacer == True:
            if starting_node.parent.right == None:
                starting_node.parent.height -= 1
            elif starting_node.parent.left == None: # has value -1
                starting_node.parent.height -= 1


            self.replacer_parent = starting_node.parent
            if starting_node.parent.left == starting_node:
                starting_node.parent.left = None
            else:
                starting_node.parent.right = None
            starting_node = None
        return starting_node

"""
t = AVLTree()
t.insert(1)
t.insert(2)
t.remove(1)
t.to_array()

q = AVLTree()
q.insert(5)
q.insert(18)
q.insert(2)
q.insert(8)
q.insert(14)
q.insert(16)
q.insert(13)
q.insert(3)
q.insert(12)
q.insert(21)
q.insert(1)
q.insert(0)
q.to_array()
print('before')
q.remove(5)
q.to_array()
print('after')

e = AVLTree()
e.insert(5)
e.insert(3)
e.insert(7)
e.insert(6)
e.insert(8)
e.to_array()
e.to_array()

print('e before')
e.remove(8)
e.to_array()
print('e after')
"""