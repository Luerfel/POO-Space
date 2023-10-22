import pygame
import os
import time
import random

from ship import Ship

class Player(Ship): # class player is inherited from the class Ship
    def __init__(self, x, y, hp=100, speed, lives, level):
        super().__init__(self, x, y, hp)
        self.img = pygame.image.load(os.path.join("assets", "main_ship.png"))
        self.speed = speed
        self.lives = lives
        self.level = level

