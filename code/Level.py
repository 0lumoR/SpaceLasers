import pygame

from code.Const import WIDTH
from code.EntityFactory import EntityFactory


class Menu:
    def __init__(self, window):
        self.window = window
        self.bg_layers = EntityFactory.get_backgrounds()
        self.font = pygame.font.Font("./assets/kenvector_future.ttf", 40)
        self.title_font = pygame.font.Font("./assets/kenvector_future.ttf", 70)
        self.selected = 0
        self.player_img = pygame.image.load("./assets/player.png").convert_alpha()
        self.player_rect = self.player_img.get_rect(center=(WIDTH//2, 650 - 100))

    def run(self):
        pygame.mixer.music.load("./assets/levelsong.mp3")
        pygame.mixer.music.play(-1)

        while True:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()



