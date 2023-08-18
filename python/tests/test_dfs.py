import unittest

from src.dfs.ice import ice

class TestDFS(unittest.TestCase):

    def test_ice(self):
        self.assertEqual(ice([[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]), 3)