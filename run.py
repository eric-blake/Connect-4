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

def is_valid_move():
    pass

def get_row():
    pass


def make_move():
    pass

def check_if_winner():
    pass


def play_game():
    game_over = False     
    while not game_over:
        try:
            if turns % 2 == 0:
                column = int(input(f" Please choose a column (1-{BOARD_COLS}): "))
                           
            else:
                pass 
            
                       
        except:
            print("Please choose a number between 1 and 7:")


play_game()