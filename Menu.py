import pygame
import sys
from button import Button

class MainMenu:
    def __init__(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Space Invaders")
        self.BG = pygame.image.load("assets/Menu_Background.png")

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def main_menu(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            MENU_TEXT = self.get_font(80).render("Space Invaders", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
            PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), text_input="PLAY", font=self.get_font(60), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), text_input="OPTIONS", font=self.get_font(60), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), text_input="QUIT", font=self.get_font(60), base_color="#d7fcd4", hovering_color="White")
            self.SCREEN.blit(MENU_TEXT, MENU_RECT)
            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        # Iniciar o jogo
                        return
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        # Abrir tela de opções
                        pass
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()

