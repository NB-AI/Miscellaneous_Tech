import unittest

from lfsr import Lfsr


class TestAssignment01ex02Student(unittest.TestCase):
    def test_result_of_lfsr(self):
        lfsr = Lfsr()
        self.assertEqual(lfsr.a5_rand(), 17, "ERROR: 1st random number wrong, should be 17")
        self.assertEqual(lfsr.a5_rand(), 16, "ERROR: 1st random number wrong, should be 16")
        self.assertEqual(lfsr.a5_rand(), 23, "ERROR: 1st random number wrong, should be 23")
        self.assertEqual(lfsr.a5_rand(), 14, "ERROR: 1st random number wrong, should be 14")
        self.assertEqual(lfsr.a5_rand(), 13, "ERROR: 1st random number wrong, should be 13")
        self.assertEqual(lfsr.a5_rand(), 12, "ERROR: 1st random number wrong, should be 12")
        self.assertEqual(lfsr.a5_rand(), 19, "ERROR: 1st random number wrong, should be 19")
        self.assertEqual(lfsr.a5_rand(), 10, "ERROR: 1st random number wrong, should be 10")
        self.assertEqual(lfsr.a5_rand(), 9, "ERROR: 1st random number wrong, should be 9")
        self.assertEqual(lfsr.a5_rand(), 8, "ERROR: 1st random number wrong, should be 8")

    def test_lfsr_size(self):
        lfsr = Lfsr()

        lfsr1 = lfsr.get_lfsr1()
        self.assertIsNotNone(lfsr1)
        self.assertEqual(len(lfsr1), 19)

        lfsr2 = lfsr.get_lfsr2()
        self.assertIsNotNone(lfsr2)
        self.assertEqual(len(lfsr2), 22)

        lfsr3 = lfsr.get_lfsr3()
        self.assertIsNotNone(lfsr3)
        self.assertEqual(len(lfsr3), 23)


if __name__ == '__main__':
    unittest.main()
