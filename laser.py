import pygame
import os
import random
import math

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

class Laser:
    def __init__(self, x, y, speed, img, angle=math.pi/2):
        self.x = x
        self.y = y
        self.angle = angle

        self.__speed = speed

        laser_angle = -(self.angle * 180 / math.pi) + 90
        self.img = pygame.transform.rotate(img, laser_angle)
        self.mask = pygame.mask.from_surface(self.img) # create a mask for the laser
    
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self):
        # vector direction
        dx = math.cos(self.angle)
        dy = math.sin(self.angle)    

        # move the laser
        self.x += dx * self.__speed
        self.y += dy * self.__speed

    def isOff_screen(self, width, height):
        return self.y + self.img.get_height() >= height or self.y <= 0 or self.x + self.img.get_width() >= width + 70 or self.x <= -70
    
    def collision(self, obj):
        return collide(self, obj)
#.