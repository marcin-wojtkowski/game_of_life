import numpy as np
import pygame
import sys
import random


size = width, height = 640, 480
dead = 169, 169, 169
alive = 255, 255, 0
cell_pixel_size = 10
rows = int(height / cell_pixel_size)
columns = int(width / cell_pixel_size)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def initialize_grids():
    display = np.zeros((rows, columns))         #the grid that's going to be displayed
    buffer = np.zeros((rows, columns))          #the grid that is in memory buffer

    return display, buffer



def create_random_grid(grid):
    for r in range(rows):
        for c in range(columns):
            grid[r][c] = random.randint(0, 1)


def draw_grid(display):
    for r in range(rows):
        for c in range(columns):
            if display[r][c] == 0:
                pygame.draw.rect(screen, dead, (c * 10, r * 10, 10, 10))
            elif display[r][c] == 1:
                pygame.draw.rect(screen, alive, (c * 10, r * 10, 10, 10))

    pygame.display.flip()


def game_logic(display, buffer):
    for r in range(1, rows - 1):
        for c in range(1, columns - 1):
            total = 0
            total += display[r-1][c-1]
            total += display[r-1][c]
            total += display[r-1][c+1]

            total += display[r][c-1]
            total += display[r][c+1]

            total += display[r+1][c-1]
            total += display[r+1][c]
            total += display[r+1][c+1]


            if display[r][c] == 1:
                if total < 2:
                    buffer[r][c] = 0
                elif total == 2:
                    buffer[r][c] = 1
                elif total == 3:
                    buffer[r][c] = 1
                elif total > 3:
                    buffer[r][c] = 0
            elif display[r][c] == 0:
                if total == 3:
                    buffer[r][c] = 1


def main_loop(display, buffer):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        draw_grid(display)
        game_logic(display, buffer)
        display = buffer
        clock.tick(6)



pygame.init()
display, buffer = initialize_grids()
create_random_grid(display)
main_loop(display, buffer)
