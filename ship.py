import pygame
import os
ship_imagem = os.path.join("assets", "main_ship.png")
class Ship():
    def __init__(self, x, y, hp=100):
        self.x = x
        self.y = y
        self.hp = hp
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
    
    def draw(self, window):
        # Carrega a imagem
        image = pygame.image.load(ship_imagem)

        # Define o tamanho desejado  
        size = (100, 100)

        # Desenha diretamente a imagem redimensionada
        window.blit(pygame.transform.scale(image, size), (self.x, self.y))

