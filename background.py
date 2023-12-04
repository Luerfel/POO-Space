import pygame
import os

from enemy import Enemy
from player import Player
from buff import Buff

# this class is used to draw all the screens
class Background:
    def __init__(self, w, h, img, surface):
        self.image = img
        self.rect = self.image.get_rect()

        self.__WIN = surface
        
        self.rect_x = 0
        self.rect_y = 0
        
        self.__WIDTH = w
        self.__HEIGHT = h

    def in_game(self, player):
        # draw the background
        self.__WIN.blit(self.image, (self.rect_x, self.rect_y),
        area=(self.rect_x, self.rect_y, self.__WIDTH, self.__HEIGHT))

        font = pygame.font.SysFont('Arial', 30) # create a font
   
        lives_text = font.render(f'Lives: {player.get_lives()}', True, (255,255,255))
        level_text = font.render(f'Level: {player.get_lvl()}', True, (255,255,255))
        hp_text = font.render(f'HP: {player.hp}', True, (255,255,255))

        self.__WIN.blit(lives_text, (10,10)) 
        self.__WIN.blit(level_text, (10,40))
        self.__WIN.blit(hp_text, (10,70))

        # draw the enemies on the screen
        for enemy in Enemy.wave: 
            enemy.draw(self.__WIN)
            for laser in enemy.lasers:
                laser.draw(self.__WIN)
        
        # draw the buffs on the screen
        for buff in Buff.buffs_wave: 
            buff.draw(self.__WIN)
        
        # draw the lasers on the screen
        for laser in player.lasers: 
            laser.draw(self.__WIN)
    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)
    def lost(self):
        pygame.mixer.music.load("assets/gameover.mp3")  # Carrega o arquivo de música
        pygame.mixer.music.play(-1)  # Reproduz a música em um loop infinito
        # draw the background
        self.__WIN.blit(self.image, (self.rect_x, self.rect_y),
        area=(self.rect_x, self.rect_y, self.__WIDTH, self.__HEIGHT))


        # draw the text on the screen
        lost_text = self.get_font(80).render("YOU LOST", True, "#b68f40")

        self.__WIN.blit(lost_text, (self.__WIDTH/2 - lost_text.get_width()/2, self.__HEIGHT/2 - lost_text.get_height()/2))   
#.