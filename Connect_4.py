# Installing needed imports
import numpy as np
import pygame
import sys
import math


# Global variables needed for board creation 

BOARD_ROWS = 6
BOARD_COLUMNS = 7

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 255)


# Creating game functions 

def create_board():
    board = np.zeros((BOARD_COLUMNS, BOARD_COLUMNS))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[BOARD_ROWS - 1][col] == 0

    

def get_next_open_row(board, col):
    for r in range(BOARD_ROWS):
        if board[r][col] == 0:
            return r 

# Flipping the board so selections go to the bottom
def print_board(board):
    print(np.flip(board, 0))

# Initializing the game board
board = create_board()

# Checking the board angles to find the winning move
def winning_move(board, piece):
    # Checking for horizontal connect 4
    for c in range(BOARD_COLUMNS - 3):
        for r in range(BOARD_ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Checking for verticle connect 4
    for c in range(BOARD_COLUMNS):
        for r in range(BOARD_ROWS -3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Checking for positive slant connect 4
    for c in range(BOARD_COLUMNS - 3):
        for r in range(BOARD_ROWS - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # Checking for negative slant connect 4
    for c in range(BOARD_COLUMNS - 3):
        for r in range(3, BOARD_ROWS):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

# Setting the continous game loop
game_over = False
turn = 0

while not game_over:
    # Asking for player input
    if turn == 0:
        col = int(input("Player One's Turn: "))
        
        if is_valid_location(board, col):
            row =  get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

            if winning_move(board, 1):
                print("Player 1 wins")
                game_over = True
    
    else:
        col = int(input("Player Two's Turn: "))

        if is_valid_location(board, col):
            row =  get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if winning_move(board, 2):
                print("Player 21 wins")
                game_over = True
        

    
    print_board(board)


    turn += 1 
    turn = turn % 2






