import numpy as np
import pygame
import sys
import random

size = width, height = 640, 480
dead = 169, 169, 169
alive = 55, 255, 0
cell_pixel_size = 10
rows = int(height / cell_pixel_size)
columns = int(width / cell_pixel_size)
screen = pygame.display.set_mode(size)

grid = np.zeros((rows, columns))

for r in range(rows):
    for c in range(columns):
        grid[r][c] = random.randint(0, 1)

print(grid)


pygame.init()

for r in range(rows):
    for c in range(columns):
        if grid[r][c] == 0:
            pygame.draw.rect(screen, dead, (r * 10, c * 10, 10, 10))
        elif grid[r][c] == 1:
            pygame.draw.rect(screen, alive, (r * 10, c * 10, 10, 10))




#pygame.blit()

pygame.display.flip()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
