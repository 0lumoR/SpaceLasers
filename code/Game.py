import pygame
from code.Const import WIDTH, HEIGHT
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Lasers")

    def run(self):
        menu = Menu(self.window)
        choice = menu.run()
        print("Escolha:", choice)
















