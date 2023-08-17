import unittest
from src.recursive.fibonacci import fibonacci, tail_fibonacci, memoization_fibonacci
from src.recursive.maximum import maximum, tail_maximum
from src.recursive.take import take, tail_take

class TestRecursive(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(tail_fibonacci(10), 55)
        self.assertEqual(memoization_fibonacci(10), 55)

    def test_maximum(self):
        self.assertEqual(maximum([1, 2, 3, 4, 5]), 5)
        self.assertEqual(tail_maximum([1, 2, 3, 4, 5]), 5)

    def test_take(self):
        self.assertEqual(take(3, [1, 2, 3, 4, 5]), [1, 2, 3])
        self.assertEqual(tail_take(3, [1, 2, 3, 4, 5]), [1, 2, 3])
        