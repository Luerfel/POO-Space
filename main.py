import pygame
import os
import time
import random

from ship import Ship
from player import Player


pygame.init()

# set a window
WIDTH, HEIGHT = 950, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders - Projeto Final")

# background image
BG = pygame.transform.scale(pygame.image.load(os.path.join("POO-Space/assets", "background.jpg")), (WIDTH, HEIGHT))
# caso der erro no de cima, usar o seguinte -> "BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.jpg")), (WIDTH, HEIGHT))"

def main(): # main program

    def draw_inGame_window(lives = 5, lvl = 1):
        WIN.blit(BG, (0,0))

        # create labels
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        lvl_label = main_font.render(f"Level: {lvl}", 1, (255,255,255))

        # draw labels
        WIN.blit(lives_label, (10, 10))
        WIN.blit(lvl_label, (WIDTH - lvl_label.get_width() - 10, 10))

        pygame.display.update() 

    run = True
    FPS = 52 # for some reasonn, any value above 52 the ship starts blinking
    clock = pygame.time.Clock()

    # create text fonts
    main_font = pygame.font.SysFont("comicsansms", 50)

    # create main objects useds in the game
    player = Player(5, 5, 1)
    ship = Ship(WIDTH/2, HEIGHT/2)

    while run:
        clock.tick(FPS)

        # check if the game is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        # movement of the ship
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and ship.x - player.speed > 0: # move left
            ship.x -= player.speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and ship.x + player.speed + 50 < WIDTH: # move right
            ship.x += player.speed  
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and ship.y + player.speed > 0: # move up
            ship.y -= player.speed  
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and ship.y - player.speed + 50 < HEIGHT: # move down
            ship.y += player.speed   
     
        draw_inGame_window(lives=player.lives, lvl=player.level)
        ship.draw(WIN)

        pygame.display.update()

main()