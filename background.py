import pygame
import os

from enemy import Enemy
from player import Player

class Background:
    def __init__(self, w, h, img, surface):
        self.image = img
        self.rect = self.image.get_rect()

        self.__WIN = surface
        
        self.rect_x = 0
        self.rect_y = 0
        
        self.__WIDTH = w
        self.__HEIGHT = h

        
    def draw(self, player):
        # draw the background
        self.__WIN.blit(self.image, (self.rect_x, self.rect_y),
        area=(self.rect_x, self.rect_y, self.__WIDTH, self.__HEIGHT))

        font = pygame.font.SysFont('Arial', 30) # create a font
   
        lives_text = font.render(f'Lives: {player.get_lives()}', True, (255,255,255))
        level_text = font.render(f'Level: {player.get_lvl()}', True, (255,255,255))

        self.__WIN.blit(lives_text, (10,10)) 
        self.__WIN.blit(level_text, (10,40))

        # draw the enemies on the screen
        for enemy in Enemy.wave: 
            enemy.draw(self.__WIN)
    
    def lost(self):
        # draw the background
        self.__WIN.blit(self.image, (self.rect_x, self.rect_y),
        area=(self.rect_x, self.rect_y, self.__WIDTH, self.__HEIGHT))

        font = pygame.font.SysFont('Arial', 60) # create a font

        # draw the text on the screen
        lost_text = font.render(f'You lost!', True, (255,255,255))
        self.__WIN.blit(lost_text, (self.__WIDTH/2 - lost_text.get_width()/2, self.__HEIGHT/2 - lost_text.get_height()/2))

    
    def update(self):
        speed = 1

   