from copy import deepcopy
from typing import List, Tuple
import time

from sudoku_dfs.merge_move import (
    populate_board_with_possible_move,
    populate_board_with_possible_move_smart,
)
from sudoku_dfs.possible_moves import get_board_possible_moves
from sudoku_dfs.validation import (
    is_complete_board,
    is_valid_board,
)


def depth_first_search(board: List[List[int]]) -> Tuple[List[List[int]], bool]:
    """A function to solve the sudoku board!

    Args:
        board (List[List[int]]): the sudoku board

    Returns:
        board_copy / board (List[List[int]]): the solved board, or input board if unable to solve
        is_solved (bool): if the sudoku board is solved or not
    """
    board_copy = deepcopy(board)
    possible_moves = get_board_possible_moves(board=board_copy)
    update_occured = True
    move_history: List[Tuple[List[List[int]], List[List[List[int]]]]] = []

    while not is_complete_board(board=board_copy):
        board_copy, possible_moves, update_occured = populate_board_with_possible_move(
            board=board_copy, possible_moves=possible_moves
        )
        # if we updated, we want to find the next move and restart
        if update_occured:
            possible_moves = get_board_possible_moves(board=board_copy)
            continue

        (
            board_copy,
            possible_moves,
            update_occured,
        ) = populate_board_with_possible_move_smart(
            board=board_copy, possible_moves=possible_moves
        )
        # if we updated, we want to find the next move and restart
        if update_occured:
            possible_moves = get_board_possible_moves(board=board_copy)
            continue

        # if update did not occure, that means thats theres multiple choices, and it's time to brute force with a depth first search
        time.sleep(0.1)

        # if the board is not valid and we have no move history, that then means that this is a bad board which can't be solved
        if (
            not is_valid_board(board=board_copy, possible_moves=possible_moves)
        ) and not move_history:
            return board, False

        # if the board is not valid, that means that we reached a dead end and need to go back one layer in our depth first search
        # NOTE unlike before, we do not get_board_possible_moves. This is because we do not want to overwrite the moves that are loaded
        if not is_valid_board(board=board_copy, possible_moves=possible_moves):
            board_copy = deepcopy(move_history[-1][0])
            possible_moves = deepcopy(move_history[-1][1])
            del move_history[-1]
            continue

        # if the board is valid, that means that we are at a fork in the road and must select a path for our depth first search
        x_position = -1
        y_position = -1
        guess_move = -1
        early_exit = False
        # itterating over the moves till we see a move with a two or more options
        for row_index, row in enumerate(possible_moves):
            for column_index, column in enumerate(row):
                if len(column) < 2:
                    continue
                y_position = row_index
                x_position = column_index
                guess_move = column[0]
                early_exit = True
                break
            if early_exit:
                break
        # removing the guessed move from our list of moves
        possible_moves[y_position][x_position].remove(guess_move)
        # storing our board and updated possible moves, incase we need to backtrack
        move_history.append((deepcopy(board_copy), deepcopy(possible_moves)))
        # updating the board with the guessed move
        board_copy[y_position][x_position] = guess_move
        # Finding new possible moves
        possible_moves = get_board_possible_moves(board=board_copy)

    return board_copy, True
