import random

def display_board(board):
    print('---------')
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
    print('---------')

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_tie(board):
    return all([cell != ' ' for row in board for cell in row])

def player_move(board, player):
    while True:
        move = input(f"Player {player}, enter your move (row and column, e.g., 1 1): ").split()
        if len(move) != 2 or not all(m.isdigit() for m in move):
            print("Invalid input. Please enter row and column numbers.")
            continue
        row, col = map(int, move)
        if row < 1 or row > 3 or col < 1 or col > 3 or board[row - 1][col - 1] != ' ':
            print("Invalid move. The cell is already occupied or out of range.")
            continue
        board[row - 1][col - 1] = player
        break

def computer_move(board, player):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    row, col = random.choice(empty_cells)
    board[row][col] = player
    print(f"Computer chose: {row + 1} {col + 1}")

def tic_tac_toe():
    board = initialize_board()
    current_player = 'X'
    opponent = 'O'
    mode = input("Enter '1' for single player or '2' for two players: ").strip()
    
    while True:
        display_board(board)
        if mode == '1' and current_player == opponent:
            computer_move(board, current_player)
        else:
            player_move(board, current_player)
        
        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break
        
        current_player, opponent = opponent, current_player

if __name__ == "__main__":
    tic_tac_toe()
