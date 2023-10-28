import pygame
import os
import math

from ship import Ship

class Player(Ship):
    # initialize the class
    def __init__(self,  x, y, speed, ship_img, hp=100):
        super().__init__(x, y, ship_img, hp)
        self.speed = speed 

        self.size = (70, 70)
        self.ship_img = pygame.transform.scale(self.ship_img, self.size)
        self.ship_img = pygame.transform.rotate(self.ship_img, -90)

        self.__lives = 5 
        self.__lvl = 0
    
    # move the ship
    def move_ship(self, keys, WIDTH=1280, HEIGHT=720):
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x - self.speed > 0: # move left
            self.x -= self.speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x + self.speed + 50 < WIDTH: # move rigth
            self.x += self.speed  
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.y + self.speed > 0: # move up
            self.y -= self.speed  
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.y - self.speed + 50 < HEIGHT: # move down
            self.y += self.speed 
    
    # overrides the parent class draw method
    def draw(self, window, cursor_pos):
        size = (70, 70) # size of the ship

        # get the center point of the image
        center_x = self.x + self.size[0] / 2
        center_y = self.y + self.size[1] / 2
        center = (center_x, center_y)

        # calculate the angle between the ship and the cursor
        dx = cursor_pos[0] - center_x
        dy = cursor_pos[1] - center_y
        angle = math.atan2(dy, dx) * 180 / math.pi

        # rotate the ship image
        rotated_img = pygame.transform.rotate(self.ship_img, -angle)
        new_rect = rotated_img.get_rect(center = center)

        # draw and rotate the ship
        window.blit(rotated_img, new_rect.topleft)

    # going through next level
    def increment_lvl(self):
        self.__lvl += 1	
    
    # losing lives
    def decrement_lives(self):
        self.__lives -= 1

    # get the values of the atributes    
    def get_lives(self):
        return self.__lives

    def get_lvl(self):
        return self.__lvl
