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


def initialize_grids():
    display = np.zeros((rows, columns))         #the grid that's going to be display
    buffer = np.zeros((rows, columns))          #the grid that is in memory buffer

    return display, buffer



def create_random_grid(grid):
    for r in range(rows):
        for c in range(columns):
            grid[r][c] = random.randint(0, 1)


def draw_grid(grid):
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 0:
                pygame.draw.rect(screen, dead, (c * 10, r * 10, 10, 10))
            elif grid[r][c] == 1:
                pygame.draw.rect(screen, alive, (c * 10, r * 10, 10, 10))

    pygame.display.flip()


def game_logic(display, buffer):
    for r in range(1, rows - 1):
        for c in range(1, columns - 1):
            total = (
            display[r-1][c-1] +
            display[r-1][c] +
            display[r-1][c+1] +

            display[r][c-1] +
            display[r][c+1] +

            display[r+1][c-1] +
            display[r+1][c] +
            display[r+1][c+1] )


            if display[r][c] == 1:
                buffer[r][c] = 0
            elif display[r][c] == 0:
                buffer[r][c] = 1
            else:
                print('Error with logic')

            '''elif display[r][c] == 1 and total == 2:
                buffer[r][c] = 1
            elif display[r][c] == 1 and total > 3:
                buffer[r][c] = 0
            elif display[r][c] == 0 and total == 3:
                buffer[r][c] = 1'''

    return buffer


def main_loop(display, buffer):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        draw_grid(display)
        buffer = game_logic(display, buffer)
        display = buffer
        clock.tick(1)


display, buffer = initialize_grids()
create_random_grid(display)

'''
print(display)
print(buffer)

print(id(display))
print(id(buffer))
'''

main_loop(display, buffer)
