from chaining_hash_node import Chaining_Hash_Node

class Chaining_Hash_Set():

    def __init__(self, capacity = 0):
        self.hash_table = [None] * capacity # we get a list of length "capacity" with only None entries
        self.table_size = 0

    def get_hash_code(self, key, hash_table_length): # hash_table_length is the number of possible slots
        """Hash function that calculates a hash code for a given key using the modulo division.
        @param key:
        		Key for which a hash code shall be calculated according to the length of the hash table.
        @param hash_table_length:
        		Length of the hash table.
        @return:
        		The calculated hash code for the given key.
        """
        return (key % hash_table_length) # is the hash code # this gives us the position where key has to be inserted

    def get_hash_table(self):
        """(Required for testing only)
        @return the hash table.
        """
        return self.hash_table

    def set_hash_table(self, table, size):
        """(Required for testing only) Set a given hash table which shall be used.
        @param table:
        		Given hash table which shall be used.
        @param size:
        		Number of already stored keys in the given table.
        """
        self.hash_table = table
        self.table_size = size

    def get_table_size(self):
        """returns the number of stored keys (keys must be unique!).
    	 """
        return self.table_size

    def insert(self, key, data):
        """Inserts a key and returns true if it was successful. If there is already an entry with the
          same key or the hash table is full, the new key will not be inserted and false is returned.

         @param key:
         		The key which shall be stored in the hash table.
         @param data:
         		Any data object that shall be stored together with a key in the hash table.
         @return:
         		true if key could be inserted, or false if the key is already in the hash table.
         @throws:
         		a ValueError exception if any of the input parameters is None.
         """
        if key == None or data == None:
            raise ValueError('Inserted stuff is None!')

        # we need to calculate the insert position with help of the hash func.:
        hash_code_position = self.get_hash_code(key, len(self.hash_table))

        # First try of insertion into the hash_table:

        if self.hash_table[hash_code_position] == None: # the insert position in the table is empty
            self.hash_table[hash_code_position] = Chaining_Hash_Node()
            self.hash_table[hash_code_position].key = key
            self.hash_table[hash_code_position].data = data
            # Now we have also update the number of saved nodes in the table:
            self.table_size += 1
            return True

        else: # the insert position in the table is occupied
            # Lets start a recursion to check where a free place is and also if the key already exists in the table
            booler = self.recursive_chain(key, data, self.hash_table[hash_code_position])
            return booler


    def recursive_chain(self, key, data, chain_slot): #PROBLEM?? No
        if key == chain_slot.key:
            return False
        elif chain_slot.next == None: # insert the key here
            chain_slot.next = Chaining_Hash_Node()
            chain_slot.next.key = key
            chain_slot.next.data = data
            chain_slot.next.next = None
            # Now we have also update the number of saved nodes in the table:
            self.table_size += 1
            return True # we successfully inserted key in occupied node
        else: # start recursion because we have to check the next element in the overflow list
            return self.recursive_chain(key, data, chain_slot.next)

    def contains(self, key):
        """Searches for a given key in the hash table.
         @param key:
         	    The key to be searched in the hash table.
         @return:
         	    true if the key is already stored, otherwise false.
         @throws:
         	    a ValueError exception if the key is None.
         """
        if key == None:
            raise ValueError('Searched key is None!')

        # First we need the hash value to get the index where the value would be stored:
        hash_code_position = self.get_hash_code(key, len(self.hash_table))

        # Lets check if the key is already stored:
        if self.hash_table[hash_code_position] == None: # key is not stored
            return False
        else: # a key is standing where we search but which one?:

            finder = self.recursive_find(key, self.hash_table[hash_code_position])
            return finder

    def recursive_find(self, key, chain_slot):  # PROBLEM?? No
        if key == chain_slot.key:
            return True
        elif chain_slot.next == None:  # There is no longer a key coming which could be the same as our key
            return False
        else:  # start recursion because we have to check the next element in the overflow list
            return self.recursive_find(key, chain_slot.next)




    def remove(self, key):
        """Removes the key from the hash table and returns true on success, false otherwise.
        @param key:
        		The key to be removed from the hash table.
        @return:
        		true if the key was found and removed, false otherwise.
        @throws:
         	a ValueError exception if the key is None.
        """
        if key == None:
            raise ValueError('Searched key for removing is None!')

        # First find the searched key:
        hash_code_position = self.get_hash_code(key, len(self.hash_table))

        if self.hash_table[hash_code_position] == None:  # key is not stored and therefore cannot be removed
            return False

        else:  # a key is standing where we search but which one?:
            remover = self.recursive_find_remove(key, self.hash_table[hash_code_position])
            return remover

    def recursive_find_remove(self, key, chain_slot):  # PROBLEM?? No

        if key == chain_slot.key: # We find the key to remove
            if chain_slot.next != None:
                #old_chain_slot = chain_slot
                if chain_slot.next.next != None:
                    the_nexter = chain_slot.next # very important: save the next next node as extra variable. otherwise:
                    # doing chain_slot.next = chain.slot.next.next --> the next next node exists twice times as next and next next
                    chain_slot.key = chain_slot.next.key
                    chain_slot.data = chain_slot.next.data
                    chain_slot.next = the_nexter.next
                    #chain_slot = chain_slot.next

                else:
                  #  chain_slot = chain_slot.next # works out????
                    chain_slot.key = chain_slot.next.key
                    chain_slot.data = chain_slot.next.data
                    chain_slot.next.key = None
                    chain_slot.next.data = None
                    chain_slot.next = None

            else:
                chain_slot.key = None
                chain_slot.data = None
                chain_slot = None

            self.table_size -= 1 # number of stored elements get smaller
            return True

        elif chain_slot.next == None:  # There is no longer a key coming which could be the same as our key
            return False
        else:  # start recursion because we have to check the next element in the overflow list
            if chain_slot.next != None:
                return self.recursive_find_remove(key, chain_slot.next)
            else:
                print('ERROR HERE')

    def clear(self):
        """Removes all stored elements from the hash table by setting all nodes to None.
        """
        for index, key in enumerate(self.hash_table):
            if key != None:
                self.hash_table[index] = None
        self.table_size = 0
        return
"""
classy = Chaining_Hash_Set(2)
classy.insert(2, '2')
classy.insert(4, '4')
classy.insert(6, '6')
classy.insert(8, '8')
print(classy.remove(10))

print(classy.contains(2))
classy.clear()
"""