import unittest

from src.bfs.maze_escape import maze_escape

class TestBFS(unittest.TestCase):

    def test_maze_escape(self):
        self.assertEqual(maze_escape(0,0,[[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]), 10)


    