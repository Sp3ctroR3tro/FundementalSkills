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
    board = np.zeros((6,7))
    return board

def drop_piece():
    None

def is_valid_location(col):
    None

def get_next_open_row(col):
    None

# Initializing the game board
board = create_board()

# Setting the continous game loop
game_over = False
turn = 0

while not game_over:
    # Asking for player input
    if turn == 0:
        col = int(input("Player One's Turn"))
    else:
        col = int(input("Player Two's Turn"))
    turn += 1 
    turn % 2






