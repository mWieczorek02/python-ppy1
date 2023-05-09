def print_board(board):
    print(" " + board[0][0] + "|" + board[0][1] + "|" + board[0][2] + " ")
    print("==|=|==")
    print(" " + board[1][0] + "|" + board[1][1] + "|" + board[1][2] + " ")
    print("==|=|==")
    print(" " + board[2][0] + "|" + board[2][1] + "|" + board[2][2] + " ")


def check_win(board, player):
    return ((board[0][0] == player and board[0][1] == player and board[0][2] == player) or
            (board[1][0] == player and board[1][1] == player and board[1][2] == player) or
            (board[2][0] == player and board[2][1] == player and board[2][2] == player) or
            (board[0][0] == player and board[1][0] == player and board[2][0] == player) or
            (board[0][1] == player and board[1][1] == player and board[2][1] == player) or
            (board[0][2] == player and board[1][2] == player and board[2][2] == player) or
            (board[0][0] == player and board[1][1] == player and board[2][2] == player) or
            (board[0][2] == player and board[1][1] == player and board[2][0] == player))


def tic_tac_toe():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    player = 'X'
    game_over = False

    while not game_over:
        print_board(board)
        moves_str = input("Player " + player +
                          ", choose your move (1-3),(1-3): ")
        moves = moves_str.split(",")

        if board[int(moves[0])-1][int(moves[1])-1] == ' ':
            board[int(moves[0])-1][int(moves[1])-1] = player
        else:
            print("space taken.")
            continue

        if check_win(board, player):
            print_board(board)
            print("Player " + player + " wins!")
            game_over = True
        else:
            player = 'O' if player == 'X' else 'X'


if __name__ == "__main__":
    tic_tac_toe()
