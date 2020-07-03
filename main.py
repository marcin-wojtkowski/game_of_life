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


pygame.init()

grid2 = np.zeros((rows, columns))

def create_random_grid():
    grid = np.zeros((rows, columns))
    for r in range(rows):
        for c in range(columns):
            grid[r][c] = random.randint(0, 1)

    return grid



arg = create_random_grid()


def draw_grid(grid):
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 0:
                pygame.draw.rect(screen, dead, (c * 10, r * 10, 10, 10))
            elif grid[r][c] == 1:
                pygame.draw.rect(screen, alive, (c * 10, r * 10, 10, 10))

    pygame.display.flip()


def game_logic(grid):
    for r in range(1, rows - 1):
        for c in range(1, columns - 1):
            total = (
            grid[r-1][c-1] +
            grid[r-1][c] +
            grid[r-1][c+1] +

            grid[r][c-1] +
            grid[r][c+1] +

            grid[r+1][c-1] +
            grid[r+1][c] +
            grid[r+1][c+1] )


            if grid[r][c] == 1 and total < 2:
                grid2[r][c] = 0
            elif grid[r][c] == 1 and (total == 2 or total == 3):
                grid2[r][c] = 1
            elif grid[r][c] == 1 and total > 3:
                grid2[r][c] = 0
            elif grid[r][c] == 0 and total == 3:
                grid2[r][c] = 1
            else:
                print('Error with logic')

    return grid2





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    draw_grid(arg)
    arg = game_logic(arg)
    clock.tick(1)
