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

def create_random_grid():
    grid = np.zeros((rows, columns))

    for r in range(rows):
        for c in range(columns):
            grid[r][c] = random.randint(0, 1)

    return grid

def draw_grid(grid):
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 0:
                pygame.draw.rect(screen, dead, (c * 10, r * 10, 10, 10))
            elif grid[r][c] == 1:
                pygame.draw.rect(screen, alive, (c * 10, r * 10, 10, 10))

    pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    arg = create_random_grid()
    draw_grid(arg)
    clock.tick(2)
