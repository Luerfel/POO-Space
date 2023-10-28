import pygame
import os
import math

from ship import Ship

class Enemy(Ship):
    wave = []
    wave_length = 5

    speed_increment = 0 # the amount of speed that will be added to the enemies after each wave

    # dictionary of colors of the enemies and their images (ship_img, laser_img)
    COLOR_MAP = {
        "red": (pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png")), pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))),
        "green": (pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png")), pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))),
        "blue": (pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png")), pygame.image.load(os.path.join("assets", "pixel_laser_blue.png")))
    }
    
    def __init__(self, x, y, color, hp=100): # "red", "gren", "blue"
        super().__init__(x, y, hp)

        self.ship_img, self.laser_img = self.COLOR_MAP[color] # get the images from the dictionary
        self.mask = pygame.mask.from_surface(self.ship_img) # create a mask for the enemies

        self.speed = (1 + self.speed_increment) if (color == "red") else ( (1.5 + self.speed_increment) if (color == "green") else (2 + self.speed_increment) ) # set the speed of the enemies | red = 1, green = 2, blue = 3

    # method to move the enemies
    def move(self):
        self.y += self.speed