import pygame
import os
import math

from ship import Ship
from laser import Laser

class Enemy(Ship):
    wave = [] # wave of enemies
    wave_length = 5

    speed_increment = 0 # the amount of speed that will be added to the enemies after each wave

    # dictionary of colors of the enemies and their images (ship_img, laser_img)
    LASERIMG = pygame.transform.scale(pygame.transform.rotate(pygame.image.load(os.path.join("assets", "spr_EnemyBullet.png")), 90), (15, 25))
    COLOR_MAP = {
        "red": (pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png")), LASERIMG),
        "green": (pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png")), LASERIMG),
        "blue": (pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png")), LASERIMG)
    }
    
    def __init__(self, x, y, color, hp=100): # "red", "gren", "blue"
        super().__init__(x, y, None, hp)
        self.__color = color

        self.ship_img, self.laser_img = self.COLOR_MAP[color] # get the images from the dictionary
        self.mask = pygame.mask.from_surface(self.ship_img) # create a mask for the enemies

        self.speed = (1 + self.speed_increment) if (color == "red") else ( (1.5 + self.speed_increment) if (color == "green") else (2 + self.speed_increment) ) # set the speed of the enemies | red = 1, green = 2, blue = 3

    # method to move the enemies
    def move(self):
        self.y += self.speed
    
    def shoot(self): # shoot the lasers
        posx = self.x + self.COLOR_MAP[self.__color][0].get_width() / 2 - self.COLOR_MAP[self.__color][1].get_width() / 2
        posy = self.y + self.COLOR_MAP[self.__color][0].get_height() / 2 - self.COLOR_MAP[self.__color][1].get_height() / 2

        if self.cd_counter == 0:
            laser = Laser(x=posx, y=posy, speed=6, img=self.laser_img)
            self.lasers.append(laser)
            self.cd_counter = 1
#.