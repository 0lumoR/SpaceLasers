import pygame
from code.Const import WIDTH, HEIGHT
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Lasers")

    def run(self):
        running = True
        while running:
            menu = Menu(self.window)
            option = menu.run()

            if option == "START GAME":
                level = Level(self.window,'Level 1',option)
                level.run()

                print("Iniciar jogo (aqui vai a lógica do gameplay futuramente)")

            elif option == "HOW TO PLAY":
                print("Mostrar instruções")

            elif option == "SCORE":
                print("Mostrar placar")

            elif option == "EXIT":
                running = False

        pygame.quit()












