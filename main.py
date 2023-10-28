import pygame
import os
import time
import random

from background import Background
from player import Player
from enemy import Enemy

pygame.init()

WIDTH, HEIGHT = 1280, 720  
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Space Invaders")

def main_game():

    background = Background(pygame.image.load(os.path.join("assets", "background.jpg")))

    run = True
    FPS = 60
    clock = pygame.time.Clock()
    player = Player(WIDTH/2, HEIGHT/2, 5, pygame.image.load(os.path.join("assets", "main_ship.png")))  # create the player

    while run :
        clock.tick(FPS)
        
        # check of the game is closed
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        if len(Enemy.wave) == 0:    # if there are no enemies (https://miro.medium.com/v2/resize:fit:958/1*P9xAw_nF6ohqlKMFpgcoxA.jpeg)
            
            # create the enemies
            for i in range(Enemy.wave_length):
                enemy = Enemy(random.randint(50, WIDTH - 50), random.randint(-1500, -100), random.choice(["red", "green", "blue"]), random.choice([100, 150, 200]))
                Enemy.wave.append(enemy)

            player.increment_lvl()  # go to the next level
            Enemy.wave_length += 5  # increase the number of enemies
            Enemy.speed_increment += 0.2 # increase the speed of the enemies
            
        background.draw(WIN, player.get_lives(), player.get_lvl()) # draw the background

        player.move_ship(pygame.key.get_pressed()) # move the ship
        player.draw(WIN, pygame.mouse.get_pos()) # draw the ship

        for enemy in Enemy.wave: # go through the enemies
            enemy.draw(WIN)
            enemy.move()
            if enemy.y + enemy.get_height() > HEIGHT:
                player.decrement_lives()
                Enemy.wave.remove(enemy)    # remove the enemy from the list of enemies

        pygame.display.update() # update the display

main_game()