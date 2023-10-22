import pygame
import os

class Background:
    def __init__(self, filename):
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        
        self.rect_x = 0
        self.rect_y = 0

        
    def draw(self, surface):
        # Desenhar apenas uma região da imagem
        surface.blit(self.image, (self.rect_x, self.rect_y),
        area=(self.rect_x, self.rect_y, 1280, 720))
    
    def update(self):
        speed = 1

