from random import randint
import time

BOARD_COLS = 7
BOARD_ROWS = 6
turns = 0


def welcome():
    """Prints the welcome message and prompts the user for their name"""
    print("Welcome to Connect-4 game")
    print("\n")
    name = input("What is your name? \n ")
    print("\n")
    # isalpha method from stack overflow
    while not name.isalpha() or len(name) < 2:
        print("invalid name, please enter 2 or mroe letters only")
        name = input("What is your name? \n")
    print('Hello ' + name)
    print("\n")
    return name


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
    #return board[BOARD_ROWS-1][column] == " "
    return True
    


def get_row(board, column):
    """check board for empty row and return that row"""
    for row in range(BOARD_ROWS-1,-1,-1): 
        if board[row][column] == " ":
            return row
    return False   
    


def make_move(board, row, column, chip):
    """Drop chip in selected slot"""
    board[row][column] = chip
    print_board()
  

def check_if_winner():
    pass


def play_game():
    welcome()
    game_over = False     
    while not game_over:
        try:
            global turns
            if turns % 2 == 0:
                column = int(input(f" Please choose a column (1-{BOARD_COLS}): \n"))
                if is_valid_move(board, column):
                    row = get_row(board, column)
                    make_move(board, row, column,'🟡' )
                    turns += 1
                           
            else:
                print("Computers move next")
                print("\n")
                time.sleep(3)
                column = random_number()
                if is_valid_move(board, column):
                    row = get_row(board, column,)
                    make_move(board, row, column,'🔴')
                    turns += 1

        except:
            print("Please choose a number between 1 and 7:")
        game_over = check_if_winner()


def random_number():
    """Random number generated for computers move"""
    return randint(0, BOARD_COLS - 1)        

play_game()