import unittest

from src.programmers.find_prime import find_prime
from src.programmers.word_conversion import word_conversion
from src.programmers.furthest_node import furthest_node
from src.programmers.travel_route import travel_route
from src.programmers.sheep_and_wolves import sheep_and_wolves
from src.programmers.personal_information_validity_period import (
    personal_information_validity_period,
)
from src.programmers.matrix_operations import matrix_operations


class TestGreedy(unittest.TestCase):
    def test_find_prims(self):
        self.assertEqual(find_prime("17"), 3)
        self.assertEqual(find_prime("011"), 2)

    def test_word_conversion(self):
        self.assertEqual(
            word_conversion("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4
        )
        self.assertEqual(
            word_conversion("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0
        )

    def test_furthest_node(self):
        self.assertEqual(
            furthest_node(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]),
            3,
        )

    def test_travel_route(self):
        self.assertEqual(
            travel_route([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]),
            ["ICN", "JFK", "HND", "IAD"],
        )
        self.assertEqual(
            travel_route(
                [
                    ["ICN", "SFO"],
                    ["ICN", "ATL"],
                    ["SFO", "ATL"],
                    ["ATL", "ICN"],
                    ["ATL", "SFO"],
                ]
            ),
            ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"],
        )

    def test_sheep_and_wolves(self):
        self.assertEqual(
            sheep_and_wolves(
                [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
                [
                    [0, 1],
                    [1, 2],
                    [1, 4],
                    [0, 8],
                    [8, 7],
                    [9, 10],
                    [9, 11],
                    [4, 3],
                    [6, 5],
                    [4, 6],
                    [8, 9],
                ],
            ),
            5,
        )
        self.assertEqual(
            sheep_and_wolves(
                [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
                [
                    [0, 1],
                    [0, 2],
                    [1, 3],
                    [1, 4],
                    [2, 5],
                    [2, 6],
                    [3, 7],
                    [4, 8],
                    [6, 9],
                    [9, 10],
                ],
            ),
            5,
        )

    def test_personal_information_validity_period(self):
        self.assertEqual(
            personal_information_validity_period(
                "2022.05.19",
                ["A 6", "B 12", "C 3"],
                ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"],
            ),
            [1, 3],
        )
        self.assertEqual(
            personal_information_validity_period(
                "2020.01.01",
                ["Z 3", "D 5"],
                [
                    "2019.01.01 D",
                    "2019.11.15 Z",
                    "2019.08.02 D",
                    "2019.07.01 D",
                    "2018.12.28 Z",
                ],
            ),
            [1, 4, 5],
        )

    def test_matrices_operations(self):
        self.assertEqual(
            matrix_operations(
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]
            ),
            [[8, 9, 6], [4, 1, 2], [7, 5, 3]],
        )
        self.assertEqual(
            matrix_operations(
                [[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]
            ),
            [[8, 3, 3], [4, 9, 7], [3, 8, 6]],
        )
        self.assertEqual(
            matrix_operations(
                [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                ["ShiftRow", "Rotate", "ShiftRow", "Rotate"],
            ),
            [[1, 6, 7, 8], [5, 9, 10, 4], [2, 3, 12, 11]],
        )
