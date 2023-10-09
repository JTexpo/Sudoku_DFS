from typing import List


# FINDING POSSIBLE MOVES : TILE SUB CHECK
# ---------------------------------------
def possible_width_moves(board: List[List[int]], y_position: int) -> List[int]:
    """A function to find all the valid moves that exists in a row

    Args:
        board (List[List[int]]): the sudoku board
        y_position (int): which row to find all avaible numbers

    Returns:
        List[int]: a list of avaible numbers
    """
    all_moves = list(range(1, 10))
    for column in board[y_position]:
        if column in all_moves:
            all_moves.remove(column)
    return all_moves


def possible_height_moves(board: List[List[int]], x_position: int) -> List[int]:
    """A function to find all the valid moves that exists in a column

    Args:
        board (List[List[int]]): the sudoku board
        x_position (int): which column to find all avaible numbers

    Returns:
        List[int]: a list of avaible numbers
    """
    all_moves = list(range(1, 10))
    for row in board:
        if row[x_position] in all_moves:
            all_moves.remove(row[x_position])
    return all_moves


def possible_box_moves(
    board: List[List[int]], box_row: int, box_column: int
) -> List[int]:
    """A function to find all the valid moves that exists in a box

    Args:
        board (List[List[int]]): the sudoku board
        box_row (int): a number 0 -> 2, where the box is located across
        box_column (int): a number 0 -> 2, where the box is located tall

    Returns:
        List[int]: a list of avaible numbers
    """
    all_moves = list(range(1, 10))
    for row in range(box_row * 3, box_row * 3 + 3):
        for column in range(box_column * 3, box_column * 3 + 3):
            if board[row][column] in all_moves:
                all_moves.remove(board[row][column])
    return all_moves


# FINDING POSSIBLE MOVES : TILE
# -----------------------------
def get_tile_possible_moves(
    board: List[List[int]], x_position: int, y_position: int
) -> List[int]:
    """A abstract function to call the possible moves and merge together their responses to give all legal moves a tile can make

    Args:
        board (List[List[int]]): the sudoku board
        x_position (int): the column (x) location of the tile
        y_position (int): the row (y) location of the tile

    Returns:
        List[int]: a list of avaible numbers
    """

    # if the board already has a value in its tile
    if board[y_position][x_position] != 0:
        return []

    # merging together all possible moves
    return list(
        set(possible_width_moves(board=board, y_position=y_position))
        & set(possible_height_moves(board=board, x_position=x_position))
        & set(
            possible_box_moves(
                board=board, box_row=y_position // 3, box_column=x_position // 3
            )
        )
    )


# FINDING POSSIBLE MOVES : ALL
# ----------------------------
def get_board_possible_moves(board: List[List[int]]) -> List[List[List[int]]]:
    """A function to get all of the possible moves for the board

    Args:
        board (List[List[int]]): the sudoku board

    Returns:
        List[List[List[int]]]: the sudoku board with labels for all possible moves ex.
            [
            [ [1,2,3], [2,3], [5,9], ... ],
            ...
            ]
    """

    # creating a blank list for the board
    prediction_board: List[List[List[int]]] = []
    # itterating through the rows of the board
    for row_index, row in enumerate(board):
        # adding a new row to the prediction
        prediction_board.append([])
        # itterating through the columns of the board
        for column_index, column in enumerate(row):
            # finding the tiles possible moves and adding it to the predictions
            prediction_board[row_index].append(
                get_tile_possible_moves(
                    board=board, x_position=column_index, y_position=row_index
                )
            )
    return prediction_board
