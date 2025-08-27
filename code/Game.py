import pygame
from code.Const import WIDTH, HEIGHT
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Lasers")

    def run(self):
        while True:
            menu = Menu(self.window)
            choice = menu.run()
            if choice == "START GAME":
                level = Level(self.window, 'Level 1', choice)
                level.run()

                print("Iniciar jogo (aqui vai a lógica do gameplay futuramente)")

            elif choice == "HOW TO PLAY":
                print("Mostrar instruções")

            elif choice == "SCORE":
                print("Mostrar placar")

            elif choice == "EXIT":
                running = False

            pygame.quit()


















