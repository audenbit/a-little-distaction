# A game by Audenbit (Fiad Muntakim) Under the MIT license.

import pygame
import os

WIDTH = 900
HEIGHT = 600

# initialize pygame
pygame.init()

# set window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Makes closing the game not a hassle
game_on = True
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
