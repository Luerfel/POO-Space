import pygame
import os
import time
import random

pygame.init()

# set a window
WIDTH, HEIGHT = 950, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders - Projeto Final")

# background image
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.jpg")), (WIDTH, HEIGHT))

def main(): # main program
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    # create text fonts
    main_font = pygame.font.SysFont("comicsansms", 50)
    
    def draw_inGame_window(lives = 5, lvl = 1):
        WIN.blit(BG, (0,0))

        # create labels
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        lvl_label = main_font.render(f"Level: {lvl}", 1, (255,255,255))

        # draw labels
        WIN.blit(lives_label, (10, 10))
        WIN.blit(lvl_label, (WIDTH - lvl_label.get_width() - 10, 10))

        pygame.display.update() 

    while run:
        clock.tick(FPS)
        # check if the game is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        draw_inGame_window()

main()