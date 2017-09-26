#TicTacToo Project
import os
def display_board(board):
    os.system('clear')
    print ('\n\n')
    print("       |   |")
    print("     " + board[1] + " | " + board[2] + " | " + board[3])
    print("       |   |")
    print("    ---+---+---")
    print("       |   |")
    print("     " + board[4] + " | " + board[5] + " | " + board[6])
    print("       |   |")
    print("    ---+---+---")
    print("       |   |")
    print("     " + board[7] + " | " + board[8] + " | " + board[9])
    print("       |   |")

def space_check(board, position):
    if board[position] == ' ':
        return True
    return False

def player_input(marker, board):
    position = ' '
    while(position not in "1 2 3 4 5 6 7 8 9".split() or not space_check(board, int(position))):
        print('\nNext move is for : ', marker)
        position = input("Choose your next position [1-9] : ")
    return int(position)

def place_marker(board, marker, position):
    board[position] = marker
    return board

def win_check(board, marker):
    #winning combinations are [1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9] and [3,5,7]
    winning_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    for trio in winning_combinations:
        if board[trio[0]] == board[trio[1]] == board[trio[2]] == marker:
            print('\n Game over!!\n ' + marker + ' is the winner!! \n\n')
            return True
    return False

import random
def choose_first():
    if random.randint(0,1) == 0:
        return "X"
    else:
        return "O"

def full_board_check(board):
    for position in range(1,10):
        if board[position] != 'X' and board[position] != 'O':
            return False
    print('\nGame over!!\nIts a draw!!')
    return True

def player_choice():
    return (input("Do you want to play (yes/no): ").upper().startswith('Y'))

def replay():
    pass

board = [0,' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

#display_board(board)

print('Welcome to Tic Tac Toe!')

# while True:
while (True):
    if not player_choice():
        break
    board = [0,' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board([0,'1', '2', '3', '4', '5', '6', '7', '8', '9'])
    marker = choose_first()
    while not ( full_board_check(board) or win_check(board, 'X') or win_check(board, 'O')):
        position = player_input(marker, board)
        place_marker(board, marker, position)
        if marker == 'X':
            marker = 'O'
        else:
            marker = 'X'
        display_board(board)
