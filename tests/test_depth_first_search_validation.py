import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")

import unittest
from sudoku_solver.depth_first_search.validation import is_complete_board


class DepthFirstSearchValidation(unittest.TestCase):
    # is_complete_board
    # --------------------
    def test_is_complete_board_complete(self):
        # Arrange
        board = [
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

        # Act
        result = is_complete_board(board=board)

        # Assert
        self.assertTrue(result)

    def test_is_complete_board_not_complete(self):
        # Arrange
        board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        # Act
        result = is_complete_board(board=board)

        # Assert
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
