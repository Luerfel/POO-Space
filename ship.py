import pygame
import os

class Ship():
    # initialize the class
    def __init__(self, x, y, ship_img, hp=100):
        self.x = x
        self.y = y
        self.hp = hp
        
        self.ship_img = ship_img
    
    def draw(self, window):
        size = (70, 70) # size of the ship

        window.blit(self.ship_img, (self.x, self.y)) # draw the ship

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

