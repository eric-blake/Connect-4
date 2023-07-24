from random import randint
import time

BOARD_COLS = 7
BOARD_ROWS = 6
turns = 0


def welcome():
    """Prints the welcome message and prompts the user for their name"""
    print("Welcome to Connect-4 game")
    print("\n")
    global name
    name = input("Please enter your name? \n")
    print("\n")
    # isalpha method from stack overflow
    while not name.isalpha() or len(name) < 2:
        print("invalid name, please enter 2 or more letters only \n")
        name = input("What is your name? \n")
    print(f"Hello {name}, you will be playing against the computer. Take turns dropping colored tokens \n")
    print("The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of your own tokens")
    print("\n")
    return name


def make_board():
    """Sets the board size"""
    board = [[" " for column in range(BOARD_COLS)]
             for row in range(BOARD_ROWS)]
    return board


board = make_board()
game_over = False


def print_board():
    """Print out board grid using bars and dashed line"""
    for column in range(BOARD_COLS):
        print(f"   {column + 1}  ", end="")
    for row in range(BOARD_ROWS):
        print(f" \n {'-' * (BOARD_COLS * 6)}")
        print('|', end="")
        for column in range(BOARD_COLS):
            print(f" {board[row][column]}   |", end="")
    print(f" \n {'-' * (BOARD_COLS * 6)}")
    print("\n")
    return board


def is_valid_move(board, column):
    """check if top column is free, if true then make move"""
    if board[BOARD_ROWS-6][column] == " ":
        return True
    return False


def get_row(board, column):
    """check board for empty row and return that row"""
    for row in range(BOARD_ROWS-1, -1, -1):
        if board[row][column] == " ":
            return row
    return False


def make_move(board, row, column, chip):
    """Drop chip in selected slot"""
    board[row][column] = chip
    print_board()


def check_if_winner():
    """Check if four in a row and return winner"""
    # Check horizontal axis for winner
    for row in range(BOARD_ROWS):
        for column in range(BOARD_COLS - 3):
            if (board[row][column] == '🟡'
                    and board[row][column + 1] == '🟡'
                    and board[row][column + 2] == '🟡'
                    and board[row][column + 3] == '🟡'):
                print(f" Congratulations {name} - You Win!")
                return True
            elif (board[row][column] == '🔴'
                    and board[row][column + 1] == '🔴'
                    and board[row][column + 2] == '🔴'
                    and board[row][column + 3] == '🔴'):
                print(f" Hard luck {name} - Computer Wins")
                return True

    # Check vertical axis for winner
    for row in range(BOARD_ROWS - 3):
        for column in range(BOARD_COLS):
            if (board[row][column] == '🟡'
                    and board[row + 1][column] == '🟡'
                    and board[row + 2][column] == '🟡'
                    and board[row + 3][column] == '🟡'):
                print(f" Congratulations {name} - You Win!")
                return True
            elif (board[row][column] == '🔴'
                    and board[row + 1][column] == '🔴'
                    and board[row + 2][column] == '🔴'
                    and board[row + 3][column] == '🔴'):
                print(f" Hard luck {name} - Computer Wins")
                return True

    # Check diagonal-right grid for winner
    for row in range(BOARD_ROWS - 3):
        for column in range(BOARD_COLS - 3):
            if (board[row][column] == '🟡'
                    and board[row + 1][column + 1] == '🟡'
                    and board[row + 2][column + 2] == '🟡'
                    and board[row + 3][column + 3] == '🟡'):
                print(f" Congratulations {name} - You Win!")
                return True
            elif (board[row][column] == '🔴'
                    and board[row + 1][column + 1] == '🔴'
                    and board[row + 2][column + 2] == '🔴'
                    and board[row + 3][column + 3] == '🔴'):
                print(f" Hard luck {name} - Computer Wins")
                return True

    # Check diagonal-left grid for winner
    for row in range(BOARD_ROWS - 3):
        for column in range(BOARD_COLS - 3):
            if (board[row][column] == '🟡'
                    and board[row + 1][column - 1] == '🟡'
                    and board[row + 2][column - 2] == '🟡'
                    and board[row + 3][column - 3] == '🟡'):
                print(f" Congratulations {name} - You Win!")
                return True

            elif (board[row][column] == '🔴'
                    and board[row + 1][column - 1] == '🔴'
                    and board[row + 2][column - 2] == '🔴'
                    and board[row + 3][column - 3] == '🔴'):
                print(f" Hard luck {name} - Computer Wins")
                return True

    return False


def play_game():
    welcome()
    print_board()
    game_over = False
    while not game_over:
        try:
            global turns
            if turns % 2 == 0:
                column = int(input
                             (f" Please choose a column (1-{BOARD_COLS}): \n"))
                if is_valid_move(board, column):
                    row = get_row(board, column)
                    make_move(board, row, column, '🟡')
                    turns += 1

            else:
                print("Computers move next - Please wait")
                print("\n")
                # time delay from Stack overflow
                time.sleep(2)
                column = random_number()
                if is_valid_move(board, column):
                    row = get_row(board, column)
                    make_move(board, row, column, '🔴')
                    turns += 1

        except:
            print(" Incorrect entry:\n")
        game_over = check_if_winner()

        if not any(' ' in row for row in board):
            print("Game over - Draw")
            return


def random_number():
    """Random number generated for computers move"""
    return randint(0, BOARD_COLS - 1)


play_game()
