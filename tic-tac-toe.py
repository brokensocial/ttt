import os


def init_board():
    """Returns an empty 3-by-3 board (with zeros)."""

    board = [
        [0, 0, 0,],
        [0, 0, 0,],
        [0, 0, 0,],
    ]
    return board


def get_move(board, player):
<<<<<<< HEAD
    #Returns the coordinates of a valid move for player on board."""

    row, col = 0, 0
=======
    """Returns the coordinates of a valid move for player on board."""
    input_is_not_valid = True
    rows = ["A", "B", "C"]
    columns = ["1", "2", "3"]
    while input_is_not_valid:
        user_input = input("Please enter coordinates player " + str(player) + ": ").upper()
        print()
        if len(user_input) > 2:  # validate input length
            print("Please enter valid coordinates player " + str(player) + " (e.g. A1, B3) !\n")
        elif not user_input[0].isalpha() or not user_input[1].isdecimal():  # validate if input is alpha and decimal
            print("Please enter valid coordinates player " + str(player) + " (e.g. A1, B3) !\n")
        elif not user_input[0] in rows or not user_input[1] in columns:  # validate if input is in board borders
            print("Please enter valid coordinates player " + str(player) + " (e.g. A1, B3) !\n")
        else:
            row_index = rows.index(user_input[0])
            column_index = columns.index(user_input[1])
            if board[row_index][column_index] != 0:  # validate if input is already on board
                print("Please enter valid coordinates player " + str(player) + " (e.g. A1, B3) !\n")
            else:
                input_is_not_valid = False  # input is OK
    row, col = row_index, column_index
>>>>>>> bf7360c36b67acc91c9e424e729578f37f1d3bcf
    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    board[row][col] = player


def has_won(board, player):
    if(
    board[0][0] == board[0][1] == board[0]][2] or
    board[1][0] == board[1][1] == board[1]][2] or
    board[2][0] == board[2][1] == board[2]][2] or
    board[0][0] == board[1][0] == board[2]][0] or
    board[0][1] == board[1][1] == board[2]][1] or
    board[0][2] == board[1][2] == board[2]][2] or
    board[0][0] == board[1][1] == board[2]][2] or
    board[2][0] == board[1][1] == board[0]][2]):
        return True
    return False


def is_full(board):
    """Returns True if board is full."""
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    pass


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    os.system("clear")
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':

    main_menu()