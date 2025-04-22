from open_hash_node import Open_Hash_Node

class Double_Hash_Set():

    def __init__(self, capacity = 0):
        self.hash_table = [None] * capacity
        self.table_size = 0

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

    # from me added function
    def get_hash_code(self, key, hash_table_length): # hash_table_length is the number of possible slots
        """Hash function that calculates a hash code for a given key using the modulo division.
        @param key:
        		Key for which a hash code shall be calculated according to the length of the hash table.
        @param hash_table_length:
        		Length of the hash table.
        @return:
        		The calculated hash code for the given key.
        """
        return (key % hash_table_length)

    def get_hash_code_2(self, key, hash_table_length):
        """Hash function 2 for double hashing, that calculates a key specific offset.
        @param key:
        		Key for which a hash code shall be calculated according to the length of the hash table.
        @param hash_table_length:
        		Length of the hash table.
        @return:
        		The calculated hash code for the given key.
        """
        return 1 + key % (hash_table_length-1)

    def combi_h1_h2(self, h1, h2, hash_table_length):
        return (h1 + h2) % hash_table_length

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
        elif self.table_size == len(self.hash_table): # the table is already full
            return False
        # Calculate the first hash value to get position in the table:
        h1 = self.get_hash_code(key,len(self.hash_table))


        # Call the inserting function that searches index and insert at the right one:
        inserted = self.search_place(key, data, h1)

        return inserted


    def search_place(self, key, data, h1):

        if self.hash_table[h1] == None: # then we can insert easily
            self.hash_table[h1] = Open_Hash_Node()
            self.hash_table[h1].key = key
            self.hash_table[h1].data = data
            self.hash_table[h1].removed = False # Now we have again a element in this spot, therefore we don't need removed at the moment
            self.table_size += 1 # one more element stored in table by successful insertion
            return True

        elif self.hash_table[h1].key == key: # The key is already in the table
            return False

        else: # the insertion place is occupied.
            # Calculate the second hash value to know how much step we have to go within the table:
            h2 = self.get_hash_code_2(key, len(self.hash_table))
            # Calculate the new index position for the insertion key in the table:
            new_h1 = self.combi_h1_h2(h1, h2, len(self.hash_table))
            return self.search_place(key, data, new_h1)


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
        elif self.table_size == 0: # no values in table stored
            return False

        # Calculate the first hash value to get position in the table:
        start_h1 = self.get_hash_code(key,len(self.hash_table))

        finder = self.find_place(key, start_h1, start_h1, True)
        return finder


    def find_place(self, key, h1, start_h1, first_call):

        if first_call == False and h1 == start_h1:
            # we come out at the starting position again without finding the searched key
            return False

        if self.hash_table[h1] == None:
            # the spot is not occupied and we have no need to go on further because if there would the key in the table
            # then here at the empty spot or at least at would have a marker removed = True
            return False

        elif self.hash_table[h1].key == None and self.hash_table[h1].removed == True:
            # then go on
            # Calculate the second hash value to know how much step we have to go within the table:
            h2 = self.get_hash_code_2(key, len(self.hash_table))
            # Calculate the new index position for the insertion key in the table:
            new_h1 = self.combi_h1_h2(h1, h2, len(self.hash_table))
            return self.find_place(key, new_h1, start_h1, False)

        elif self.hash_table[h1].key == key:  # We find the key
            return True

        elif self.hash_table[h1].key != key:
            # we have to search further
            # Calculate the second hash value to know how much step we have to go within the table:
            h2 = self.get_hash_code_2(key, len(self.hash_table))
            if h2 == 0:
                print('h2 is 0!')
                return False
            # Calculate the new index position for the insertion key in the table:
            new_h1 = self.combi_h1_h2(h1, h2, len(self.hash_table))
            return self.find_place(key, new_h1, start_h1, False)

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
            raise ValueError('Key to remove is None!')
        elif self.table_size == 0:  # no values in table stored
            return False

            # Calculate the first hash value to get position in the table:
        start_h1 = self.get_hash_code(key, len(self.hash_table))

        remover = self.find_to_remove(key, start_h1, start_h1, True)
        return remover

    def find_to_remove(self, key, h1, start_h1, first_call):
        if first_call == False and h1 == start_h1:
            # we come out at the starting position again without finding the searched key
            return False

        if self.hash_table[h1] == None:
            # the spot is not occupied and we have no need to go on further because if there would the key in the table
            # then here at the empty spot or at least at would have a marker removed = True
            return False

        elif self.hash_table[h1].key == None and self.hash_table[h1].removed == True:
            # then go on
            # Calculate the second hash value to know how much step we have to go within the table:
            h2 = self.get_hash_code_2(key, len(self.hash_table))
            # Calculate the new index position for the insertion key in the table:
            new_h1 = self.combi_h1_h2(h1, h2, len(self.hash_table))
            return self.find_to_remove(key, new_h1, start_h1, False)

        elif self.hash_table[h1].key == key:  # We find the key
            self.hash_table[h1] = Open_Hash_Node()
            self.hash_table[h1].removed = True # Mark the position where the key have been removed
            self.table_size -= 1
            return True

        elif self.hash_table[h1].key != key:
            # we have to search further
            # Calculate the second hash value to know how much step we have to go within the table:
            h2 = self.get_hash_code_2(key, len(self.hash_table))
            if h2 == 0:
                print('h2 is 0!')
                return False
            # Calculate the new index position for the insertion key in the table:
            new_h1 = self.combi_h1_h2(h1, h2, len(self.hash_table))
            return self.find_to_remove(key, new_h1, start_h1, False)


    def clear(self):
        """Removes all stored elements from the hash table by setting all nodes to None.
        """
        for index, node in enumerate(self.hash_table):
            if node != None:
                self.hash_table[index] = None
        self.table_size = 0
        return
"""
class2 = Double_Hash_Set(5)
class2.insert(2, '2')
class2.insert(4, '4')
class2.insert(6, '6')
print(class2.contains(5))
class2.remove(2)
class2.remove(6)
print(class2.get_table_size())
class2.clear()
"""