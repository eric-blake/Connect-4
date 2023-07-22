BOARD_COLS = 7
BOARD_ROWS = 6


def make_board():
    """Sets the board size"""
    board = [[" " for column in range(BOARD_COLS)] for row in range(BOARD_ROWS)]
    return board

board = make_board()
print(board)