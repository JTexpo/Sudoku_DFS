from copy import deepcopy
from typing import List, Tuple, Set


# MERGING DATA : BASIC
# --------------------
def populate_board_with_possible_move(
    board: List[List[int]], possible_moves: List[List[List[int]]]
) -> Tuple[List[List[int]], List[List[List[int]]], bool]:
    """A function to act on 1, and only 1 prediction at a time

    Args:
        board (List[List[int]]): the sudoku board
        possible_moves (List[List[List[int]]]): all of the possible moves that the board can have

    Returns:
        board_copy (List[List[int]]): the updated board
        possible_moves_copy (List[List[List[int]]]): the updated moves list, minus the move used
        update_occured (bool): if the board was updated or not
    """
    # creating a copy so we don't edit any data we wish to preserve
    board_copy = deepcopy(board)
    possible_moves_copy = deepcopy(possible_moves)

    # itterating over the board
    for row_index, row in enumerate(possible_moves):
        for column_index, column in enumerate(row):
            # if there is only 1 prediction, then we populate this to the board and exit
            # NOTE we do not do this more than once, because some invalid boards will have several tiles that can only have 1 move ex
            # [ [ [3], [3], [3,4,5] ,...]]
            # in the cause above, we would double populate 3, and that would not be good
            if len(column) != 1:
                continue
            board_copy[row_index][column_index] = column[0]
            possible_moves_copy[row_index][column_index] = []
            return board_copy, possible_moves_copy, True

    return board_copy, possible_moves_copy, False


# MERGING DATA : ADVANCE
# ----------------------


def advance_width_moves(
    possible_moves: List[List[List[int]]], x_position: int, y_position: int
) -> Set[int]:
    """A function to find all the valid moves that exists in a row

    Args:
        board (List[List[int]]): the sudoku board
        y_position (int): which row to find all avaible numbers

    Returns:
        List[int]: a list of avaible numbers
    """
    all_moves = set(possible_moves[y_position][x_position])

    for column_index, column in enumerate(possible_moves[y_position]):
        if column_index == x_position:
            continue
        other_moves = set(column)
        all_moves = all_moves - other_moves
        if not all_moves:
            return set([])

    return all_moves


def advance_height_moves(
    possible_moves: List[List[List[int]]], x_position: int, y_position: int
) -> Set[int]:
    """A function to find all the valid moves that exists in a row

    Args:
        board (List[List[int]]): the sudoku board
        y_position (int): which row to find all avaible numbers

    Returns:
        List[int]: a list of avaible numbers
    """
    all_moves = set(possible_moves[y_position][x_position])

    for row_index, row in enumerate(possible_moves):
        if row_index == y_position:
            continue
        other_moves = set(row[x_position])
        all_moves = all_moves - other_moves
        if not all_moves:
            return set([])

    return all_moves


def advance_box_moves(
    possible_moves: List[List[List[int]]], x_position: int, y_position: int
) -> Set[int]:
    """A function to find all the valid moves that exists in a row

    Args:
        board (List[List[int]]): the sudoku board
        y_position (int): which row to find all avaible numbers

    Returns:
        List[int]: a list of avaible numbers
    """
    all_moves = set(possible_moves[y_position][x_position])
    box_row = y_position // 3
    box_column = x_position // 3

    all_moves = list(range(1, 10))
    for row in range(box_row * 3, box_row * 3 + 3):
        for column in range(box_column * 3, box_column * 3 + 3):
            if row == box_row and column == box_column:
                continue

            other_moves = set(possible_moves[row][column])
            all_moves = all_moves - other_moves
            if not all_moves:
                return set([])

    return all_moves


def populate_board_with_possible_move_smart(
    board: List[List[int]], possible_moves: List[List[List[int]]]
) -> Tuple[List[List[int]], List[List[List[int]]], bool]:
    # creating a copy so we don't edit any data we wish to preserve
    board_copy = deepcopy(board)
    possible_moves_copy = deepcopy(possible_moves)

    # itterating over the board
    for row_index, row in enumerate(board):
        for column_index, column in enumerate(row):
            # Checking the width / high / box , to see if there is a single unique move to be made
            width_advence = advance_width_moves(
                possible_moves=possible_moves_copy,
                x_position=column_index,
                y_position=row_index,
            )
            if len(width_advence) == 1:
                board_copy[row_index][column_index] = list(width_advence)[0]
                possible_moves_copy[row_index][column_index] = []
                return board_copy, possible_moves_copy, True
            height_advence = advance_height_moves(
                possible_moves=possible_moves_copy,
                x_position=column_index,
                y_position=row_index,
            )
            if len(height_advence) == 1:
                board_copy[row_index][column_index] = list(height_advence)[0]
                possible_moves_copy[row_index][column_index] = []
                return board_copy, possible_moves_copy, True
            box_advence = advance_height_moves(
                possible_moves=possible_moves_copy,
                x_position=column_index,
                y_position=row_index,
            )
            if len(box_advence) == 1:
                board_copy[row_index][column_index] = list(box_advence)[0]
                possible_moves_copy[row_index][column_index] = []
                return board_copy, possible_moves_copy, True

            # Checking merged permutations of the width / height / box , to see if there is a shared unique move to be made
            width_by_height = width_advence & height_advence
            if len(width_by_height) == 1:
                board_copy[row_index][column_index] = list(width_by_height)[0]
                possible_moves_copy[row_index][column_index] = []
                return board_copy, possible_moves_copy, True
            width_by_box = width_advence & box_advence
            if len(width_by_height) == 1:
                board_copy[row_index][column_index] = list(width_by_box)[0]
                possible_moves_copy[row_index][column_index] = []
                return board_copy, possible_moves_copy, True
            height_by_box = height_advence & box_advence
            if len(width_by_height) == 1:
                board_copy[row_index][column_index] = list(height_by_box)[0]
                possible_moves_copy[row_index][column_index] = []
                return board_copy, possible_moves_copy, True

            # Checking merged of the width / height / box , to see if there is a shared unique move to be made
            all_advance = width_advence & height_advence & box_advence
            if len(width_by_height) == 1:
                board_copy[row_index][column_index] = list(all_advance)[0]
                possible_moves_copy[row_index][column_index] = []
                return board_copy, possible_moves_copy, True

    return board_copy, possible_moves_copy, False
