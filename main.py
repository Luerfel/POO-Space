import pygame
import os
import time
import random
import sys

from background import Background
from player import Player
from enemy import Enemy
from buff import Buff
from laser import collide
from Menu import MainMenu

pygame.init()

# variables and constants that'll be used to run the game window ----------------------------------------------------------------------
WIDTH, HEIGHT = 1280, 720  
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Space Invaders")

background = Background(WIDTH, HEIGHT, pygame.image.load(os.path.join("assets", "background.jpg")), WIN)


def main_game():
    # variables and constants that'll be used in the game ----------------------------------------------------------------------------
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    pygame.mixer.music.load("assets/shakira.mp3")  # Carrega o arquivo de música
    pygame.mixer.music.play(-1)  # Reproduz a música em um loop infinito
    pygame.mixer.music.set_volume(0.3)  # Define o volume para a metade (0.0 é silencioso, 1.0 é o volume máximo)
    # create the player
    PLAYER_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("assets", "main_ship.png")), (70,70))
    player = Player(WIDTH/2 - (PLAYER_SHIP.get_width()/2), HEIGHT - 100, PLAYER_SHIP)  

    # functions that'll be used in the game ------------------------------------------------------------------------------------------
    def isClosed(): # check if the game is closed
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                return True
        return False
    


    def next_lvl(): # go to the next level
        # create the enemies
        for i in range(Enemy.wave_length):
            enemy = Enemy(random.randint(50, WIDTH - 50), random.randint(-1500, -100), random.choice(["red", "green", "blue"]), random.choice([100, 150, 200]))
            Enemy.wave.append(enemy)

        # create the buffs
        for i in range(Buff.wave_length):
            # buff = Buff(random.randint(50, WIDTH - 50), random.randint(-800, -50), random.choice(["atackspeed", "fasterBullets", "speed", "moreLives", "piercingBullets", "shield", "laser"]))
            buff = Buff(random.randint(50, WIDTH - 50), random.randint(-800, -50), random.choice(["atackspeed", "fasterBullets", "piercingBullets", "moreLives"]))
            Buff.buffs_wave.append(buff)

        player.increment_lvl()  # go to the next level
        Enemy.speed_increment += 0.1 # increase the speed of the enemies
        Enemy.wave_length += 5 # increase amount of enemies per wave
        Buff.wave_length += 1 # increase amount of buffs per wave
        Buff.speed_increment += 0.1 # increase the speed of the buffs to match the enemies

    # call the start screen
    tela_inicio = MainMenu()
    tela_inicio.main_menu()

    # main game loop -----------------------------------------------------------------------------------------------------------------

    while run:
        clock.tick(FPS)
        
        if isClosed():
            pygame.quit()
            run = False
        
        if len(Enemy.wave) == 0: # if there are no enemies (https://miro.medium.com/v2/resize:fit:958/1*P9xAw_nF6ohqlKMFpgcoxA.jpeg)
            next_lvl()

        if player.get_lives() <= 0: # if the player lost all lives
            pygame.mixer.music.stop()  # Para a música quando sair do menu
            background.lost()
            pygame.display.update()
            time.sleep(10)
            run = False
        
        if player.hp <= 0: # if the player lost all hp
            player.decrement_lives()
            player.hp = 100

        background.in_game(player) # draw the background

        player.move_ship(pygame.key.get_pressed(),  pygame.mouse.get_pos(),WIDTH, HEIGHT) # move the ship
        player.draw(WIN, pygame.mouse.get_pos()) # draw the ship

        # go through the enemies 
        for enemy in Enemy.wave: 
            enemy.move() # move the enemy
            enemy.move_lasers(player, HEIGHT, WIDTH) # move the lasers
            if random.randrange(0, 2*FPS) == 1: # 50% of chance to shoot every second
                enemy.shoot()
                

            if collide(enemy, player): # if the enemy collides with the player
                player.decrement_lives()
                Enemy.wave.remove(enemy)

            elif enemy.y + enemy.get_height() > HEIGHT: # if the enemy is off screen
                player.decrement_lives()
                Enemy.wave.remove(enemy) 
        
        # go through the buffs
        for buff in Buff.buffs_wave:
            buff.move() # move the buff
            buff.run_timer() # run the timer of the buff
            player.buff_player() # check if the active buffs

            if collide(buff, player): # if the buff collides with the player
                Buff.buffs_wave.remove(buff)

                match buff.type:
                    case "atackspeed":
                        Buff.buff_Timer[buff.type] = 10*FPS # adds 10 seconds of buff
                        player.buff_player(buff) # applies the buff to the player
                    case "fasterBullets":
                        Buff.buff_Timer[buff.type] = 10*FPS # adds 10 seconds of buff
                        player.buff_player(buff) # applies the buff to the player
                    case "speed":
                        Buff.buff_Timer[buff.type] = 10*FPS # adds 10 seconds of buff
                        player.buff_player(buff) # applies the buff to the player
                    case "moreLives":
                        # doesnt need a timer, since its not an effect
                        player.buff_player(buff) # applies the buff to the player
                    case "piercingBullets":
                        Buff.buff_Timer[buff.type] = 10*FPS # adds 10 seconds of buff
                        player.buff_player(buff) # applies the buff to the player
                    case "shield":
                        pass
                    case "laser":
                        pass
            
            elif buff.y + buff.get_height() > HEIGHT: # if is off screen
                Buff.buffs_wave.remove(buff)

        player.move_lasers(Enemy.wave, HEIGHT, WIDTH) # move the lasers

        pygame.display.update() # update the display

main_game()
#.