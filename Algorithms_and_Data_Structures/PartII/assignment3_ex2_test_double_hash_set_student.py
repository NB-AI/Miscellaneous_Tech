import unittest

from double_hash_set import Double_Hash_Set
from open_hash_node import Open_Hash_Node

test_table_size = 9
test_table_1 = [Open_Hash_Node(6,"6"), Open_Hash_Node(14,"14"), None,
                Open_Hash_Node(1,"1"), Open_Hash_Node(42,"42"), None,
                Open_Hash_Node(19,"19"), None,
                Open_Hash_Node(21,"21"), Open_Hash_Node(8,"8"),
                Open_Hash_Node(10,"10"),Open_Hash_Node(11,"11"), None]

class TestDoubleHashSetStudent(unittest.TestCase):
    def insert(self, set, key):
        return set.insert(int(key), str(key))

    def contains(self, set, key):
        return set.contains(int(key))

    def remove(self, set, key):
        return set.remove(int(key))

    def test_size_with_insert_duplicates(self):
        set = Double_Hash_Set(capacity = 17)

        self.assertTrue(self.insert(set, 5))
        self.assertEqual(1, set.get_table_size())
        self.assertFalse(self.insert(set, 5))
        self.assertEqual(1, set.get_table_size())


    def test_get_hash_table(self):
        set = Double_Hash_Set(capacity = 11)
        hash_table = set.get_hash_table()
        for n in hash_table:
            self.assertTrue(n == None)


    def test_contains(self):
        global test_table_1, test_table_size

        set = Double_Hash_Set(capacity = 1)
        set.set_hash_table(test_table_1, test_table_size)
        test_arr_true = [6,14,1,42,19,21,8,10]
        test_arr_false = [15,111,2]

        for i in test_arr_true:
            self.assertTrue(self.contains(set, i), ".contains("+str(i)+") returned FALSE for the following hash table:\n"
            + "\n"+self.print_list(set.get_hash_table())+"\t")

        for i in test_arr_false:
            self.assertFalse(self.contains(set, i), ".contains("+str(i)+") returned TRUE for the following hash table:\n"
            + "\n"+self.print_list(set.get_hash_table())+"\t") # my correction

    def print_list(self, list):
        sb = "\t"+"{:>10}".format("Index:")
        i = 0
        while i< len(list):
            sb+= "{:4d}|".format(i)
            i+=1
        sb +="\n\t"
        sb +="{:>10}".format("Key:")
        i = 0
        while i< len(list):
            if list[i] != None:
                sb+= "{:4d}|".format(list[i].key)
            else:
                sb+="    |"
            i+=1
        sb +="\n\t"
        sb +="{:>10}".format("Flags:")
        i = 0
        while i< len(list):
            if list[i] != None:
                sb+= "{:>4}|".format("T" if list[i].removed else "F")
            else:
                sb+="{:>4}|".format("")
            i+=1
        sb +="\n"
        return sb


if __name__ == '__main__':
    unittest.main()
