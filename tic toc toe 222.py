def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(s == player for s in row):
            return True
 
    return False
def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    while True:
        print_board(board)
        player = players[turn % 2]
        try:
            row, col = map(int, input(f"Player {player}, enter row and column (0-2) separated by space: ").split())
            board[row][col] = player
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            turn += 1
        except (ValueError, IndexError):
            print("Invalid input. Please enter two numbers between 0 and 2.")
if __name__ == "__main__":
    tic_tac_toe()