import os
from random import randint


def init_board():
    """Returns an empty 3-by-3 board (with zeros)."""

    board = [
        [0, 0, 0,],
        [0, 0, 0,],
        [0, 0, 0,],
    ]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    input_is_not_valid = True
    rows = ["A", "B", "C"]
    columns = ["1", "2", "3"]
    current_player = "X" if player == 1 else "O"
    while input_is_not_valid:
        user_input = input("Please enter coordinates player " + current_player + ": ").upper()
        print()
        if user_input == "QUIT":
            os.sys.exit(0)
        elif len(user_input) != 2:  # validate input length
            print("Please enter valid coordinates player " + current_player + " (e.g. A1, B3) !\n")
        elif not user_input[0].isalpha() or not user_input[1].isdecimal():  # validate if input is alpha and decimal
            print("Please enter valid coordinates player " + current_player + " (e.g. A1, B3) !\n")
        elif not user_input[0] in rows or not user_input[1] in columns:  # validate if input is in board borders
            print("Please enter valid coordinates player " + current_player + " (e.g. A1, B3) !\n")
        else:
            row_index = rows.index(user_input[0])
            column_index = columns.index(user_input[1])
            if board[row_index][column_index] != 0:  # validate if input is already on board
                print("Please enter valid coordinates player " + current_player + " (e.g. A1, B3) !\n")
            else:
                input_is_not_valid = False  # input is OK
    row, col = row_index, column_index
    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    possible_moves = []
    row_index = 0
    for row in board:
        column_index = 0
        for column in row:
            if column == 0:
                possible_moves.append(tuple((row_index, column_index)))
            column_index += 1
        row_index += 1
    draw_random_move = randint(0, len(possible_moves) - 1)
    random_move = possible_moves[draw_random_move]

    (row, col) = random_move
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    board[row][col] = player


def has_won(board, player):
    """Returns True if player has won the game."""
    if(
    board[0][0] == board[0][1] == board[0][2] == player or
    board[1][0] == board[1][1] == board[1][2] == player or
    board[2][0] == board[2][1] == board[2][2] == player or
    board[0][0] == board[1][0] == board[2][0] == player or
    board[0][1] == board[1][1] == board[2][1] == player or
    board[0][2] == board[1][2] == board[2][2] == player or
    board[0][0] == board[1][1] == board[2][2] == player or
    board[2][0] == board[1][1] == board[0][2] == player):
        return True
    return False


def is_full(board):
    """Returns True if board is full."""
    number_of_taken_fields_on_board = 0
    for row in board:
        for col in row:
            if col != 0:
                number_of_taken_fields_on_board += 1
    if number_of_taken_fields_on_board == 9:
        return True
    else:
        return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    rows_string = []
    board_as_table = []
    for row in board:
        board_as_table.append(row.copy())
    row_index = 0
    for row in board_as_table:
        col_index = 0
        for col in row:
            if col == 0:
                board_as_table[row_index][col_index] = "."
            elif col == 1:
                board_as_table[row_index][col_index] = "X"
            elif col == 2:
                board_as_table[row_index][col_index] = "O"
            col_index += 1
        row_index += 1
    header = "   1   2   3 \n"
    conjuctioner = "  ---+---+---"
    for row in board_as_table:
        rows_string.append(" " + row[0] + " | " + row[1] + " | " + row[2] + " ")
    print(header)
    print("A " + rows_string[0])
    print(conjuctioner)
    print("B " + rows_string[1])
    print(conjuctioner)
    print("C " + rows_string[2] + "\n")


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if(winner == 1):
        print("X won!\n")
    elif winner == 2:
        print("O won!\n")
    elif(winner == 0):
        print("It's a tie!\n")


def tictactoe_game(mode='HUMAN-HUMAN'):
    os.system("clear")
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    current_move_number = 0
    max_number_of_moves = 9
    current_player = 1
    first_player = 1
    second_player = 2
    tie = 0
    while(current_move_number < max_number_of_moves and not has_won(board, current_player) and not is_full(board)):
        current_player = first_player if current_move_number % 2 == 0 else second_player
        print_board(board)
        if mode == 'HUMAN-HUMAN':
            row, col = get_move(board, current_player)
        elif mode == 'HUMAN-AI':
            if current_player == first_player:
                row, col = get_move(board, current_player)
            elif current_player == second_player:
                row, col = get_ai_move(board, current_player)
        os.system("clear")
        mark(board, current_player, row, col)
        current_move_number = current_move_number + 1
    if(has_won(board, first_player)):
        winner = first_player
    elif(has_won(board, second_player)):
        winner = second_player
    elif is_full(board):
        winner = tie
    print_board(board)
    print_result(winner)


def main_menu():
    os.system("clear")
    input_mode = input("Available modes:\n\n1: 'HUMAN-HUMAN'\n\n2: 'HUMAN-AI'\n\nPlease choose mode: ")
    tictactoe_game('HUMAN-HUMAN') if input_mode == "1" else tictactoe_game('HUMAN-AI')


if __name__ == '__main__':

    main_menu()
