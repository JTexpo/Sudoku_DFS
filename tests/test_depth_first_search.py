import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")

import unittest
from sudoku_solver.depth_first_search.depth_first_search import depth_first_search


class DepthFirstSearch(unittest.TestCase):
    # depth_first_search
    # ------------------
    def test_depth_first_search_easy(self):
        # Arrange
        board = [
            [5, 0, 0, 4, 6, 7, 3, 0, 9],
            [9, 0, 3, 8, 1, 0, 4, 2, 7],
            [1, 7, 4, 2, 0, 3, 0, 0, 0],
            [2, 3, 1, 9, 7, 6, 8, 5, 4],
            [8, 5, 7, 1, 2, 4, 0, 9, 0],
            [4, 9, 6, 3, 0, 8, 1, 7, 2],
            [0, 0, 0, 0, 8, 9, 2, 6, 0],
            [7, 8, 2, 6, 4, 1, 0, 0, 5],
            [0, 1, 0, 0, 0, 0, 7, 0, 8],
        ]

        # Act
        result, _ = depth_first_search(board=board)

        # Assert
        expected = [
            [5, 2, 8, 4, 6, 7, 3, 1, 9],
            [9, 6, 3, 8, 1, 5, 4, 2, 7],
            [1, 7, 4, 2, 9, 3, 5, 8, 6],
            [2, 3, 1, 9, 7, 6, 8, 5, 4],
            [8, 5, 7, 1, 2, 4, 6, 9, 3],
            [4, 9, 6, 3, 5, 8, 1, 7, 2],
            [3, 4, 5, 7, 8, 9, 2, 6, 1],
            [7, 8, 2, 6, 4, 1, 9, 3, 5],
            [6, 1, 9, 5, 3, 2, 7, 4, 8],
        ]
        self.assertTrue(expected == result)

    # def test_depth_first_search_blank(self):
    #     # this is very intense on the PC for obvious reasons 32 guess moves , so i have left this commented
    #     # Arrange
    #     board = [
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     ]

    #     # Act
    #     result, _ = depth_first_search(board=board)

    #     # Assert
    #     expected = [
    #         [1, 2, 3, 4, 5, 8, 9, 6, 7],
    #         [4, 5, 8, 6, 7, 9, 1, 2, 3],
    #         [9, 6, 7, 1, 2, 3, 8, 4, 5],
    #         [2, 1, 9, 8, 3, 4, 5, 7, 6],
    #         [3, 8, 4, 5, 6, 7, 2, 1, 9],
    #         [5, 7, 6, 9, 1, 2, 3, 8, 4],
    #         [8, 9, 1, 3, 4, 6, 7, 5, 2],
    #         [6, 3, 2, 7, 8, 5, 4, 9, 1],
    #         [7, 4, 5, 2, 9, 1, 6, 3, 8],
    #     ]
    #     self.assertTrue(expected == result)


if __name__ == "__main__":
    unittest.main()
