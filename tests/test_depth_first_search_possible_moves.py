import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")

import unittest
from sudoku_solver.depth_first_search.possible_moves import (
    possible_width_moves,
    possible_height_moves,
    possible_box_moves,
    get_tile_possible_moves,
)


class DepthFirstSearchPossibleMoves(unittest.TestCase):
    # possible_width_moves
    # --------------------
    def test_possible_width_moves_empty(self):
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
        y_position = 0

        # Act
        result = possible_width_moves(board=board, y_position=y_position)
        result.sort()

        # Assert
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertTrue(expected == result)

    def test_possible_width_moves_populated(self):
        # Arrange
        board = [
            [0, 1, 0, 2, 0, 4, 0, 9, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        y_position = 0

        # Act
        result = possible_width_moves(board=board, y_position=y_position)
        result.sort()

        # Assert
        expected = [3, 5, 6, 7, 8]
        self.assertTrue(expected == result)

    # possible_height_moves
    # ---------------------
    def test_possible_height_moves_empty(self):
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
        x_position = 0

        # Act
        result = possible_height_moves(board=board, x_position=x_position)
        result.sort()

        # Assert
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertTrue(expected == result)

    def test_possible_height_moves_populated(self):
        # Arrange
        board = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [9, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 0, 0],
            [7, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        x_position = 0

        # Act
        result = possible_height_moves(board=board, x_position=x_position)
        result.sort()

        # Assert
        expected = [3, 4, 6, 8]
        self.assertTrue(expected == result)

    # possible_box_moves
    # ------------------
    def test_possible_box_moves_empty(self):
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
        box_row = 2
        box_column = 1

        # Act
        result = possible_box_moves(board=board, box_row=box_row, box_column=box_column)
        result.sort()

        # Assert
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertTrue(expected == result)

    def test_possible_box_moves_populated(self):
        # Arrange
        board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 6, 0, 1, 0, 0, 0],
            [0, 0, 0, 8, 0, 2, 0, 0, 0],
            [0, 0, 0, 7, 0, 3, 0, 0, 0],
        ]
        box_row = 2
        box_column = 1

        # Act
        result = possible_box_moves(board=board, box_row=box_row, box_column=box_column)
        result.sort()

        # Assert
        expected = [4, 5, 9]
        self.assertTrue(expected == result)

    # get_tile_possible_moves
    # -----------------------
    def test_get_tile_possible_moves_empty(self):
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
        x_position = 0
        y_position = 0

        # Act
        result = get_tile_possible_moves(
            board=board, x_position=x_position, y_position=y_position
        )
        result.sort()

        # Assert
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertTrue(expected == result)

    def test_get_tile_possible_moves_populated(self):
        # Arrange
        board = [
            [0, 0, 1, 0, 0, 4, 0, 0, 9],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 5, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [6, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        x_position = 0
        y_position = 0

        # Act
        result = get_tile_possible_moves(
            board=board, x_position=x_position, y_position=y_position
        )
        result.sort()

        # Assert
        expected = [7, 8]
        self.assertTrue(expected == result)

    def test_get_tile_possible_moves_populated_tile(self):
        # Arrange
        board = [
            [8, 0, 1, 0, 0, 4, 0, 0, 9],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 5, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [6, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        x_position = 0
        y_position = 0

        # Act
        result = get_tile_possible_moves(
            board=board, x_position=x_position, y_position=y_position
        )

        # Assert
        expected = []
        self.assertTrue(expected == result)


if __name__ == "__main__":
    unittest.main()
