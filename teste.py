# import pygame
# import os
# pygame.init()

# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Scrolling Background Tutorial")

# bg_filename = os.path.join("assets", "background.png")
# background_img = pygame.image.load(bg_filename)

# scroll_x = 0
# scroll_y = 0
# background_x = 0

# while True:
#    for event in pygame.event.get():
#       if event.type == pygame.QUIT:
#          pygame.quit()

#    # Scroll the background horizontally
#    scroll_x -= 1
#    background_x -= 1

#    #Draw the background twice to create seamless scrolling effect
#    screen.blit(background_img, (scroll_x, scroll_y))
#    screen.blit(background_img, (background_x, scroll_y))

#    #Reset the background position when it goes off screen
#    if scroll_x <= -screen_width:
#       scroll_x = screen_width

#    if background_x <= -screen_width:
#       background_x = screen_width

#    pygame.display.update()

x = 1 if 1 == 1 else 0
print(x)