from random import randint

def display_board(board):
    # if '#' in board:
        print(" " + board[1] + " " + "|" + " " + board[2] + " " + "|" + " " + board[3] + " ")
        print(" " + board[4] + " " + "|" + " " + board[5] + " " + "|" + " " + board[6] + " ")
        print(" " + board[7] + " " + "|" + " " + board[8] + " " + "|" + " " + board[9] + " ")


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
starting_board = [' ']*10
# display_board(test_board)
# display_board(starting_board)
# starting_board[5] = 'X'
# display_board(starting_board)


def player_input():
    """
    :return: OUTPUT = (Player 1 marker, Player 2 marker)
    """

    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1: Choose X or O: ").upper()
        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    # ROWS, COLUMNS and DIAGONAL checks
    return ((board[7] == board[8] == board[9] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark))


def choose_first():
    flip = randint(0, 1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # If board is full
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Please choose a position: (1-9)" ))

    return position


def replay():
    response = input("Play again? Enter Yes or No ")
    return response == 'Yes'


print("Welcome to TIC TAC TOE")

while True:
    # Play the game
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first")
    play_game = input("Ready to play? y or n ")
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # Gameplay
    while game_on:
        if turn == 'Player 1':
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place marker
            place_marker(the_board, player1_marker, position)
            # Check if they won
            result = win_check(the_board, player1_marker)
            # Check if a tie
            tie = full_board_check(the_board)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1 has won!!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE !!!")
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place marker
            place_marker(the_board, player2_marker, position)
            # Check if they won
            result = win_check(the_board, player2_marker)
            # Check if a tie
            tie = full_board_check(the_board)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Player 2 has won!!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE !!!")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break

