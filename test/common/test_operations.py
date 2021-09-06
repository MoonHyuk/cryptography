import unittest
from src.common import operations


class TestOperations(unittest.TestCase):

    def test_function(self):
        self.assertEqual(operations.extended_euclidean((1, 0)), (1, 1, 0))
        self.assertEqual(operations.extended_euclidean((0, 0)), (0, 1, 0))
        self.assertEqual(operations.extended_euclidean((0, 1)), (1, 0, 1))
        self.assertEqual(operations.extended_euclidean((2, 4)), (2, 1, 0))
        self.assertEqual(operations.extended_euclidean((13, 17)), (1, 4, -3))
        self.assertEqual(operations.extended_euclidean((75, 20)), (5, -1, 4))
        self.assertEqual(operations.extended_euclidean((20, 75)), (5, 4, -1))
        self.assertEqual(operations.extended_euclidean((2740, 1760)), (20, 9, -14))
        self.assertEqual(operations.extended_euclidean((152234111, 33229182501)), (1, -11354301490, 52017891))

    def test_mod_add_inverse(self):
        self.assertEqual(operations.mod_add_inverse(3, 8), 5)
        self.assertEqual(operations.mod_add_inverse(2, 2), 0)
        self.assertEqual(operations.mod_add_inverse(2, 3), 1)
        self.assertEqual(operations.mod_add_inverse(8, 5), 2)

    def test_mod_multi_inverse(self):
        self.assertEqual(operations.mod_multi_inverse(2, 4), None)
        self.assertEqual(operations.mod_multi_inverse(6, 8), None)
        self.assertEqual(operations.mod_multi_inverse(3, 7), 5)
        self.assertEqual(operations.mod_multi_inverse(13, 17), 4)
