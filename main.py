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

bg_filename = os.path.join("assets", "background.jpg")
background = Background(bg_filename)


run = True
FPS = 60
clock = pygame.time.Clock()
player = Player(5, 5, 1)
ship = Ship(WIDTH/2,HEIGHT/2)  # cria o objeto nave 
while run :
    clock.tick(FPS)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        
    background.draw(WIN)
        # movimento da nave
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and ship.x - player.speed > 0: # move a esquerda
        ship.x -= player.speed
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and ship.x + player.speed + 50 < WIDTH: # move para direita
        ship.x += player.speed  
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and ship.y + player.speed > 0: # move para cima
        ship.y -= player.speed  
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and ship.y - player.speed + 50 < HEIGHT: # move para baixo
        ship.y += player.speed   
    
    ship.draw(WIN)
    pygame.display.update()