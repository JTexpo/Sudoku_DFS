from typing import List

from pyscript import Element

from sudoku_dfs.depth_first_search import depth_first_search

def solve():
    # Collecting all of the Sudoku Elements to make a board
    sudoku_board:List[List[int]] = []

    for row in range(9):
        sudoku_board.append([])
        for column in range(9):
            sudoku_box = Element(f"sudoku{row}{column}")
            sudoku_number = 0
            try:
                sudoku_number = int(sudoku_box.element.value)
            except ValueError as error:
                pass
            sudoku_board[row].append(sudoku_number)

    # Solving board
    complete_board, is_solved = depth_first_search(board=sudoku_board)

    # Checking if the board has been solved.
    # If it has not, a warning is displayed
    # If it has, the board will be updated with the solution
    board_warnings = Element("board-warnings")
    if not is_solved:
        board_warnings.element.innerHTML = "WARNING : This board can not be solved"
        return
    

    for row in range(9):
        for column in range(9):
            sudoku_box = Element(f"sudoku{row}{column}")
            sudoku_box.element.value = complete_board[row][column]

    board_warnings.element.innerHTML = ""

    return

def reset():
    for row in range(9):
        for column in range(9):
            sudoku_box = Element(f"sudoku{row}{column}")
            sudoku_box.element.value = ''
    
    board_warnings = Element("board-warnings")
    board_warnings.element.innerHTML = ""

    return