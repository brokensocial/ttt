def init_board():
    #Returns an empty 3-by-3 board (with zeros)."""

    board = [
        [0, 0, 0,],
        [0, 0, 0,],
        [0, 0, 0,],
    ]
    return board


def get_move(board, player):
    #Returns the coordinates of a valid move for player on board."""

    row, col = 0, 0
    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    pass


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
