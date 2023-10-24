import pygame
import os
ship_imagem = os.path.join("assets", "main_ship.png")
class Ship():
    # initialize the class
    def __init__(self, x, y, ship_img, hp=100):
        self.x = x
        self.y = y
        self.hp = hp
        
        self.ship_img = ship_img
    
    def draw(self, window):
        size = (70, 70) # size of the ship

        window.blit(pygame.transform.scale(self.ship_img, size), (self.x, self.y)) # draw the ship


