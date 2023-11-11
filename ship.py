import pygame
import os
import math

from laser import Laser

class Ship():

    # initialize the class
    def __init__(self, x, y, ship_img, hp=100):
        self.x = x
        self.y = y
        self.hp = hp
        
        self.ship_img = ship_img

        self.laser_img = None
        self.lasers = []
        self.cd_counter = 0 # cooldown counter
        self.cd = 30 # half a second of base cooldown
    
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y)) # draw the ship
        for laser in self.lasers:
            laser.draw(window)
    
    def move_lasers(self, obj, h=720, w=1280):
        self.cooldown()
        for laser in self.lasers:
            laser.move()
            if laser.isOff_screen(w,h):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.hp -= 10
                self.lasers.remove(laser)
        
    def cooldown(self):
        if self.cd_counter >= self.cd:
            self.cd_counter = 0
        elif self.cd_counter > 0:
            self.cd_counter += 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()
#.