BOARD_COLS = 7
BOARD_ROWS = 6
turns = 0


def make_board():
    """Sets the board size"""
    board = [[" " for column in range(BOARD_COLS)] for row in range(BOARD_ROWS)]
    return board

board = make_board()
game_over = False


def print_board():
    """Print out board grid using bars and dashed line"""
    for column in range(BOARD_COLS):
        print( f"   {column + 1}  ", end="") 
    for row in range(BOARD_ROWS):
        print(f" \n {'-' * (BOARD_COLS * 6)}")
        print('|', end="")
        for column in range(BOARD_COLS):
            print(f" {board[row][column]}   |", end="")
    print(f" \n {'-' * (BOARD_COLS * 6)}")
    print("\n")
    return board
   
#print_board()

def is_valid_move(board, column):
    """check if top column is free, if true then make move"""
    return board[BOARD_ROWS-1][column] == " "
    


def get_row(board, column):
    """check board for empty row and return that row"""
    for row in range(BOARD_ROWS): 
        if board[row][column] == " ":
            return row
    return False   
    


def make_move():
    pass
  

def check_if_winner():
    pass


def play_game():
    game_over = False     
    while not game_over:
        try:
            global turns
            if turns % 2 == 0:
                column = int(input(f" Please choose a column (1-{BOARD_COLS}): "))
                if is_valid_move(board, column):
                    row = get_row(board, column)
                           
            else:
                continue
        except:
            print("Please choose a number between 1 and 7:")


play_game()