import numpy as np
from string import ascii_uppercase

board = np.zeros([8, 8], int)
pieces = { 0: ' ', 1: 'K', 2: 'Q', 3: 'B', 4: 'N', 5: 'R', 6: 'P', 7: 'k', 8: 'q', 9: 'b', 10: 'n', 11: 'r', 12: 'p' }

def main():
    start_pos()
    print_board(board)
    
    playing = True
    while playing:
        move_piece()

        playing = False

    print_board(board)

def print_board(board):
    for i in range(0, 8):
        output = f'{i + 1} '
        for j in range(0, 8):
            output += f'{pieces[board[i][j]]} '
        print(output)

    print('  A B C D E F G H')

def start_pos():
    board[1].fill(12)
    board[6].fill(6)
    board[0] = [5+6, 4+6, 3+6, 2+6, 1+6, 3+6, 4+6, 5+6]
    board[7] = [5, 4, 3, 2, 1, 3, 4, 5]

def move_piece():
    move = input("Enter move: ")

    commands = move.split(' ')
    (x1, y1) = commands[0].split(',')
    (x2, y2) = commands[1].split(',')
    
    piece = board[int(y1)][int(x1)]
    board[int(y1)][int(x1)] = 0
    board[int(y2)][int(x2)] = piece


main()