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
        # define the size of the ship
        size = (100, 100)

        # draw the ship
        window.blit(pygame.transform.scale(self.img, size), (self.x, self.y))

