import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

# Usar a classe:

background = Background("assets/background.jpg", [0,0])

def draw(self, surface):
    surface.blit(self.image, self.rect)
    