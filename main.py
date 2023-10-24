import pygame
import os
import time
import random

from background import Background
from ship import Ship
from player import Player

pygame.init()

WIDTH, HEIGHT = 1280, 720  
WIN = pygame.display.set_mode((WIDTH,HEIGHT))


pygame.display.set_caption("Space Invaders")

background = Background(pygame.image.load(os.path.join("assets", "background.jpg")))

run = True
FPS = 60
clock = pygame.time.Clock()
ship = Player(WIDTH/2, HEIGHT/2, 5, pygame.image.load(os.path.join("assets", "main_ship.png")))  # create the player

while run :
    clock.tick(FPS)

    for event in pygame.event.get(): # check of the game is closed
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        
    background.draw(WIN, ship.get_lives(), ship.get_lvl()) # draw the background

    ship.move_ship(pygame.key.get_pressed()) # move the ship
    ship.draw(WIN, pygame.mouse.get_pos()) # draw the ship

    pygame.display.update() # update the display