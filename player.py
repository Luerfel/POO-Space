import pygame
import os
import math

from ship import Ship
from laser import Laser
from buff import Buff

class Player(Ship):
    # initialize the class
    def __init__(self,  x, y, ship_img, hp=100):
        super().__init__(x, y, ship_img, hp)

        # atributes that can be upgraded
        self.cd = 25 # atack speed (the lower, the faster)
        self.bullet_speed = 10 # bullet speed
        self.bullet_size = (15, 25) # bullet size
        self.speed = 5 # speed of the ship
        
        # dictionary of the buffs
        self.isBuffed = {
            "atackspeed" : False,
            "fasterBullets" : False,
            "speed" : False,
            "moreLives" : False,
            "piercingBullets" : False,
            "shield" : False,
            "laser" : False,		
        }

        self.laser_img = pygame.image.load(os.path.join("assets", "spr_Bullet.png"))
        self.laser_img = pygame.transform.rotate(self.laser_img, -90)
        self.laser_img = pygame.transform.scale(self.laser_img, self.bullet_size)

        self.size = (70, 70)
        self.ship_img = pygame.transform.scale(self.ship_img, self.size)
        self.ship_img = pygame.transform.rotate(self.ship_img, -90)
        self.mask = pygame.mask.from_surface(self.ship_img) # create a mask for the player

        self.angle = 0

        self.__lives = 5
        self.__lvl = 0    
    
    # move the ship
    def move_ship(self, keys, cursor_pos,WIDTH=1280, HEIGHT=720):
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x - self.speed > 0:           # move left
            self.x -= self.speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x + self.speed + 50 < WIDTH: # move rigth
            self.x += self.speed                                                            
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.y + self.speed > 0:             # move up
            self.y -= self.speed  
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.y - self.speed + 50 < HEIGHT: # move down
            self.y += self.speed 
        if (keys[pygame.K_SPACE]):                                                          # shoot
            self.shoot()
    
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

        self.angle = math.atan2(dy, dx) # angle in radians
        angle = math.atan2(dy, dx) * 180 / math.pi # angle in degrees

        # rotate the ship image
        rotated_img = pygame.transform.rotate(self.ship_img, -angle)
        new_rect = rotated_img.get_rect(center = center)

        # draw and rotate the ship
        window.blit(rotated_img, new_rect.topleft)
    
    # shoot method for the player
    def shoot(self):
        posx = self.x + self.size[0] / 2 - self.laser_img.get_width() / 2
        posy = self.y + self.size[1] / 2 - self.laser_img.get_height() / 2

        if self.cd_counter == 0:
            laser = Laser(x=posx, y=posy, speed=-self.bullet_speed, img=self.laser_img, angle=self.angle + math.pi)
            self.lasers.append(laser)
            self.cd_counter = 1
    
    # move the lasers
    def move_lasers(self, objs, h=720, w=1280):
        self.cooldown()
        for laser in self.lasers:
            laser.move()
            if laser.isOff_screen(w, h):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if not self.isBuffed["piercingBullets"]:
                            self.lasers.remove(laser)

    # buff the playe
    def buff_player(self, buff=None):
        # buff the player if a buff was given, otherwise it wont do anything
        if buff != None:
            self.isBuffed[buff.type] = True

        # check if the buff is still active
        if self.isBuffed["atackspeed"]: 
            if buff != None:
                self.cd = 5
            elif Buff.buff_Timer["atackspeed"] == 0:
                self.cd = 25
                self.isBuffed["atackspeed"] = False  

        if self.isBuffed["fasterBullets"]:
            if buff != None:
                self.bullet_speed = 18
            elif Buff.buff_Timer["fasterBullets"] == 0:
                self.bullet_speed = 10
                self.isBuffed["fasterBullets"] = False

        if self.isBuffed["speed"]:
            if buff != None:
                self.speed = 8
            elif Buff.buff_Timer["speed"] == 0:
                self.speed = 5
                self.isBuffed["speed"] = False

        if self.isBuffed["moreLives"]:
            self.increment_lives()
            self.isBuffed["moreLives"] = False

        if self.isBuffed["piercingBullets"]:
            if Buff.buff_Timer["piercingBullets"] == 0:
                self.isBuffed["piercingBullets"] = False

        if self.isBuffed["shield"]:
            pass
        if self.isBuffed["laser"]:
            pass

    # go through next level
    def increment_lvl(self):
        self.__lvl += 1	
    
    # losing lives
    def decrement_lives(self):
        self.__lives -= 1

    # get more lives
    def increment_lives(self):
        self.__lives += 1

    # get the values of the atributes    
    def get_lives(self):
        return self.__lives

    def get_lvl(self):
        return self.__lvl
#.