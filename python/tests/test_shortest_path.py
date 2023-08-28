import unittest

from src.shortest_path.future_city import future_city
from src.shortest_path.telegram import telegram

class TestShortestPath(unittest.TestCase):
    
    def test_future_city(self):
        self.assertEqual(future_city(5,7,[[1,2],[1,3],[1,4],[2,4],[3,4],[3,5],[4,5],[4,5]]), 3)
        self.assertEqual(future_city(4,2,[[1,3],[2,4],[3,4]]), -1)
    
    def test_telegram(self):
        self.assertEqual(telegram(3,2,1,[[1,2,4],[1,3,2]]), (2,4))