import unittest

from src.programmers.find_prime import find_prime
from src.programmers.word_conversion import word_conversion
from src.programmers.furthest_node import furthest_node
from src.programmers.travel_route import travel_route
class TestGreedy(unittest.TestCase):
    
    def test_find_prims(self):
        self.assertEqual(find_prime("17"), 3)
        self.assertEqual(find_prime("011"), 2)       

    def test_word_conversion(self):
        self.assertEqual(word_conversion("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
        self.assertEqual(word_conversion("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)

    def test_furthest_node(self):
        self.assertEqual(furthest_node(6, [[3,6],[4,3],[3,2],[1,3],[1,2],[2,4],[5,2]]), 3)

    def test_travel_route(self):
        self.assertEqual(travel_route([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]), ["ICN", "JFK", "HND", "IAD"])
        self.assertEqual(travel_route([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]), ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
