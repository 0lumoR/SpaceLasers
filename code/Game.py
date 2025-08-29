import pygame
from code.Const import WIDTH, HEIGHT
from code.HowToPlay import HowToPlay
from code.Menu import Menu
from code.Level import Level
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Lasers")

    def run(self):
        running = True
        while running:
            # --- MENU PRINCIPAL ---
            menu = Menu(self.window)
            choice = menu.run()
            if choice == "EXIT":
                break

            # --- INICIAR LEVEL ---
            if choice == "START GAME":
                level_running = True
                while level_running:
                    level = Level(self.window, 'Level', choice)
                    result = level.run()  # retorna "TRY AGAIN", "BACK TO MENU", "EXIT"

                    if result == "TRY AGAIN":
                        continue  # reinicia o mesmo level
                    elif result == "BACK TO MENU":
                        level_running = False  # volta pro menu principal
                    elif result == "EXIT":
                        running = False
                        break

            # --- OUTRAS OPÇÕES DO MENU ---
            elif choice == "HOW TO PLAY":
                how_to_play = HowToPlay(self.window)
                how_to_play.run()  # abre tela de instruções
                # após fechar a tela, volta automaticamente ao menu
                continue

            elif choice == "SCORE":

                score_screen = Score(self.window)
                score_screen.run()

        pygame.quit()
