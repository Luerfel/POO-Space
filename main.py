import pygame
import os
import time
import random
from background import Background
from ship import Ship



pygame.init()

WIDTH, HEIGHT = 1280, 720  
WIN = pygame.display.set_mode((WIDTH,HEIGHT))


pygame.display.set_caption("Space Invaders")

bg_filename = os.path.join("assets", "background.jpg")
background = Background(bg_filename)


run = True
FPS = 60
clock = pygame.time.Clock()
ship = Ship(WIDTH/2,HEIGHT/2,5)  # cria o objeto nave 

main_font = pygame.font.SysFont("comicsansms", 50)
while run :
    clock.tick(FPS)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        
    background.draw(WIN)
    keys = pygame.key.get_pressed()

    ship.movimenta_nave(keys)
    
    ship.draw(WIN)
    pygame.display.update()