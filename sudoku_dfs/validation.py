from typing import List


# VALIDATION
# ----------
def is_valid_board(
    board: List[List[int]], possible_moves: List[List[List[int]]]
) -> bool:
    """Assuming that the input board has no illegal actions, we can compare the
    preditions to the baord to find if the board state is legal. This works because
    all tiles that are not populated should have at least 1 prediction, and if not,
    then the board is considered illegal!

    Args:
        board (List[List[int]]): the sudoku board
        possible_moves (List[List[List[int]]]): all of the possible moves that the board can have

    Returns:
        bool: if the board is legal or not
    """
    # itterating over the board
    for row_index, row in enumerate(board):
        for column_index, column in enumerate(row):
            # if the column is not 0, then the possible moves should be empty and no validation is needed
            if column != 0:
                continue
            # if there are no possible moves and the column is not 0, then the board can not be solved and is illegal
            if not possible_moves[row_index][column_index]:
                return False
    return True


def is_complete_board(board: List[List[int]]) -> bool:
    """A function to check if there are any blank tiles left on the board

    Args:
        board (List[List[int]]): the sudoku board

    Returns:
        bool: if the board is empty or not
    """
    # itterating over the board
    for row_index, row in enumerate(board):
        for column_index, column in enumerate(row):
            # the blank index is 0, and if that is there, then the board is not complete
            if column == 0:
                return False
    return True
