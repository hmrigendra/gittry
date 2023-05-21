import random

BOARD_PATH = './tic-tac-toe/board.txt'
EMPTY_BOARD = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def read_board(path):
    with open(path, 'r') as file:
        return file.read().splitlines()

def write_board(path, board):
    with open(path, 'w') as file:
        file.write('\n'.join(board))

def print_board(board):
    print('Current Board:')
    print(board[:3])
    print(board[3:6])
    print(board[6:9])

def is_move_valid(board, row, col):
    is_off_board = (row < 0 or row > 2 or col < 0 or col > 2)
    idx = row * 3 + col
    return not (is_off_board or board[idx] != ' ')

def get_move(board):
    row = int(input("Which row? (0-indexed): "))
    col = int(input("Which col? (0-indexed): "))
    if is_move_valid(board, row, col):
        return row * 3 + col
    else:
        print('Invalid move... try again')
        return get_move(board)

def find_empty_cells(board):
    return [idx for idx, cell in enumerate(board) if cell == ' ']

def play_human_turn(player, board):
    move_idx = get_move(board)
    board[move_idx] = player
    return board

def play_ai_turn(player, board):
    empty_cell_idxs = find_empty_cells(board)
    rand_idx = random.choice(empty_cell_idxs)
    board[rand_idx] = player
    return board

def play_game():
    continue_game = input("Continue? (y/n, default: y): ").lower()
    if continue_game == 'y':
        print('Continuing')
        board = read_board(BOARD_PATH)
    elif continue_game == 'n':
        print('Starting new game')
        board = EMPTY_BOARD[:]
    else:
        print('Only y and n are allowed')
        return

    print_board(board)
    winner = get_winner(board)
    if winner:
        print(f'{winner} wins!')
        return

    board = play_human_turn('x', board)
    print_board(board)
    winner = get_winner(board)
    if winner:
        print(f'{winner} wins!')
        return

    write_board(BOARD_PATH, board)
    print('Turn complete. Please commit and push the updated board file.')
    print('Pull in ~30 seconds to get the updated board for your next turn.')

play_game()
