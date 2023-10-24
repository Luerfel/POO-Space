import pygame
import os

class Background:
    def __init__(self, img):
        self.image = img
        self.rect = self.image.get_rect()
        
        self.rect_x = 0
        self.rect_y = 0

        
    def draw(self, surface, lives, lvl):
        # Desenhar apenas uma região da imagem
        surface.blit(self.image, (self.rect_x, self.rect_y),
        area=(self.rect_x, self.rect_y, 1280, 720))

        font = pygame.font.SysFont('Arial', 30)   
   
        lives_text = font.render(f'Lives: {lives}', True, (255,255,255))
        level_text = font.render(f'Level: {lvl}', True, (255,255,255))

        surface.blit(lives_text, (10,10)) 
        surface.blit(level_text, (10,40))

    
    def update(self):
        speed = 1

   