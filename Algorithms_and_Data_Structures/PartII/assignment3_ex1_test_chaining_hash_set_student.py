import unittest

from chaining_hash_set import Chaining_Hash_Set

class TestChainingHashSetStudent(unittest.TestCase):
    def insert(self, set, key):
        return set.insert(int(key), str(key))

    def contains(self, set, key):
        return set.contains(int(key))

    def remove(self, set, key):
        return set.remove(int(key))

    def test_size(self):
        set = Chaining_Hash_Set(capacity = 11)
        self.assertEqual(0, set.get_table_size())

        self.assertTrue(self.insert(set, 5))
        self.assertEqual(1, set.get_table_size())
        self.assertTrue(self.insert(set, 6))
        self.assertEqual(2, set.get_table_size())
        self.assertTrue(self.insert(set, 7))
        self.assertEqual(3, set.get_table_size())
        self.assertTrue(self.insert(set, 8))
        self.assertEqual(4, set.get_table_size())
        self.assertTrue(self.insert(set, 9))
        self.assertEqual(5, set.get_table_size())
        self.assertTrue(self.insert(set, 10))
        self.assertEqual(6, set.get_table_size())
        self.assertTrue(self.insert(set, 11))
        self.assertEqual(7, set.get_table_size())
        self.assertTrue(self.insert(set, 12))
        self.assertEqual(8, set.get_table_size())
        self.assertTrue(self.insert(set, 13))
        self.assertEqual(9, set.get_table_size())
        self.assertTrue(self.insert(set, 14))
        self.assertEqual(10, set.get_table_size())
        self.assertTrue(self.insert(set, 15))
        self.assertEqual(11, set.get_table_size())
        self.assertTrue(self.insert(set, 25))
        self.assertEqual(12, set.get_table_size())

    def test_get_hash_table(self):
        set = Chaining_Hash_Set(capacity = 11)
        hash_table = set.get_hash_table()
        for n in hash_table:
            self.assertTrue(n == None)


    def test_insert_with_chaining(self):
        set = Chaining_Hash_Set(capacity = 11)
        self.assertEqual(0, set.get_table_size())

        self.assertTrue(self.insert(set, 5))
        self.assertEqual(1, set.get_table_size())

        self.assertFalse(self.insert(set, 5))
        self.assertEqual(1, set.get_table_size())

        self.assertTrue(self.insert(set, 6))
        self.assertEqual(2, set.get_table_size())

        self.assertTrue(self.insert(set, 11))
        self.assertEqual(3, set.get_table_size())

        self.assertTrue(self.insert(set, 12))
        self.assertEqual(4, set.get_table_size())

        self.assertTrue(self.insert(set, 13))
        self.assertEqual(5, set.get_table_size())

        self.assertTrue(self.insert(set, 17))
        self.assertEqual(6, set.get_table_size())

        # check content
        hash_table = set.get_hash_table()
        # Index 0
        self.assertEqual(11, hash_table[0].key)
        self.assertEqual(None, hash_table[0].next)
        # Index 1
        self.assertEqual(12, hash_table[1].key)
        self.assertEqual(None, hash_table[1].next)
        # Index 2
        self.assertEqual(13, hash_table[2].key)
        self.assertEqual(None, hash_table[2].next)
        # Index 3
        self.assertEqual(None, hash_table[3])
        # Index 4
        self.assertEqual(None, hash_table[4])
        # Index 5
        self.assertEqual(5, hash_table[5].key)
        self.assertEqual(None, hash_table[5].next)
        # Index 6 (chaining)
        self.assertEqual(6, hash_table[6].key)
        self.assertTrue(hash_table[6].next != None)
        self.assertEqual(17, hash_table[6].next.key)
        self.assertEqual(None, hash_table[6].next.next)
        # Index 7
        self.assertEqual(None, hash_table[7])
        # Index 8
        self.assertEqual(None, hash_table[8])
        # Index 9
        self.assertEqual(None, hash_table[9])
        # Index 10
        self.assertEqual(None, hash_table[10])

    def test_clear(self):
        set = Chaining_Hash_Set(capacity = 11)
        hash_table = set.get_hash_table()

        self.assertTrue(self.insert(set, 5))
        self.assertEqual(1, set.get_table_size())
        self.assertTrue(self.insert(set, 6))
        self.assertEqual(2, set.get_table_size())
        self.assertTrue(self.insert(set, 7))
        self.assertEqual(3, set.get_table_size())

        self.assertTrue(set.get_table_size()>0)
        set.clear()
        self.assertEqual(0, set.get_table_size())

        i = 0
        while i< len(hash_table):
            self.assertEqual(None, hash_table[i])
            i+=1


if __name__ == '__main__':
    unittest.main()
