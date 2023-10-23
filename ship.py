import pygame
import os
ship_imagem = os.path.join("assets", "main_ship.png")
class Ship():
    def __init__(self, x, y,speed):
        self.x = x
        self.y = y
        self.hp = 100
        self.speed = speed
        self.lives = 5
        self.level = 1
    
    def draw(self, window):
        # Carrega a imagem
        image = pygame.image.load(ship_imagem)

        # Define o tamanho desejado  
        size = (100, 100)

        # Desenha diretamente a imagem redimensionada
        window.blit(pygame.transform.scale(image, size), (self.x, self.y))

        # movimento da nave
    def movimenta_nave(self,keys):
        WIDTH, HEIGHT = 1280, 720  
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x - self.speed > 0: # move a esquerda
            self.x -= self.speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x + self.speed + 50 < WIDTH: # move para direita
            self.x += self.speed  
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.y + self.speed > 0: # move para cima
            self.y -= self.speed  
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.y - self.speed + 50 < HEIGHT: # move para baixo
            self.y += self.speed   
    
