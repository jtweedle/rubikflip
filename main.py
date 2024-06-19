import sys
from time import sleep

import pygame

from board import Board

WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0
YELLOW = 255, 255, 0
BLUE = 0, 0, 255
SURFACE_SIZE = 480
ROUND = 1

def game_loop(loop: int):
    board = Board(4, 4, SURFACE_SIZE, BLACK, WHITE)
    board.initialze()
    while loop < 17:

        loop += 1
def driver():
    print(ROUND)

if __name__ == '__main__':
    driver()




