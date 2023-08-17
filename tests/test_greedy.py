import unittest

from src.greedy import (coin_split,
                        law_of_large_numbers, 
                        count_with_three_in_time, 
                        k_knight,
                        find_prime)

class TestGreedy(unittest.TestCase):

    def test_coin_split(self):
        self.assertEqual(coin_split(total_value=1260), 6)
        self.assertEqual(coin_split(total_value=660), 4)

    def test_law_of_large_numbers(self):
        answer1 = law_of_large_numbers((5,8,3), [2,4,5,4,6])
        self.assertEqual(answer1, 46)
        answer2 = law_of_large_numbers((5,3,3), [2,4,5,4,6])
        self.assertEqual(answer2, 18)

    def test_count_with_three_in_time(self):
        self.assertEqual(count_with_three_in_time(5), 11475)

    def test_k_knight(self):
        self.assertEqual(k_knight("a1"), 2)
    
    def test_find_prims(self):
        self.assertEqual(find_prime("17"), 3)
        self.assertEqual(find_prime("011"), 2)        
