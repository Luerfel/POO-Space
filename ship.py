import pygame
import os
import time
import random

class Ship:
    def __init__(self, x, y, hp=100):
        self.x = x
        self.y = y
        self.hp = hp
        self.img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
    
    def draw(self, window):

        # Carrega a imagem 
        image = pygame.image.load('main_ship.png')  
        size = (100, 100) 
        # Cria uma nova imagem com o tamanho ajustado 
        image = pygame.transform.scale(image, size)
        # Desenha a imagem na posição x, y
        window.blit(image, (self.x, self.y))
