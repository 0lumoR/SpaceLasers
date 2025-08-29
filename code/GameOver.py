import pygame
from code.Const import WIDTH, RED, YELLOW, GAME_OVER_OPTIONS, WHITE
from code.EntityFactory import EntityFactory
from code.DBProxy import DBProxy
import datetime


class GameOver:
    def __init__(self, window, score, elapsed_time):
        self.window = window
        self.score = score
        self.elapsed_time = elapsed_time
        self.player_name = ""  # digitado pelo jogador
        self.max_chars = 4
        self.bg_layers = EntityFactory.get_backgrounds()
        self.selected = 0
        self.input_mode = True  # True enquanto o jogador digita o nome
        self.db = DBProxy("scores.db")

    def run(self):
        pygame.mixer.music.load("./assets/menuGOsong.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if self.input_mode:
                        if event.key == pygame.K_RETURN and self.player_name:
                            self.input_mode = False
                            # salvar score no banco
                            self.db.insert_score(
                                self.player_name,
                                self.score,
                                self.elapsed_time,
                                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            )
                        elif event.key == pygame.K_BACKSPACE:
                            self.player_name = self.player_name[:-1]
                        elif len(self.player_name) < self.max_chars:
                            if event.unicode.isalnum():
                                self.player_name += event.unicode.upper()
                    else:
                        if event.key == pygame.K_DOWN:
                            self.selected = (self.selected + 1) % len(GAME_OVER_OPTIONS)
                        elif event.key == pygame.K_UP:
                            self.selected = (self.selected - 1) % len(GAME_OVER_OPTIONS)
                        elif event.key == pygame.K_RETURN:
                            return GAME_OVER_OPTIONS[self.selected]

            for bg in self.bg_layers:
                bg.update()
                self.window.blit(bg.image, bg.rect)

            self.menu_text(70, "GAME OVER", RED, (WIDTH // 2, 100))

            if self.input_mode:
                self.menu_text(40, f"Enter Name: {self.player_name}", YELLOW, (WIDTH // 2, 200))
            else:
                self.menu_text(40, f'{self.player_name}: {self.score}', YELLOW, (WIDTH // 2, 200))
                for i, option in enumerate(GAME_OVER_OPTIONS):
                    color = YELLOW if i == self.selected else WHITE
                    self.menu_text(40, option, color, (WIDTH // 2, 290 + i * 60))

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        font = pygame.font.Font("./assets/kenvector_future.ttf", text_size)
        surf = font.render(text, True, text_color).convert_alpha()
        rect = surf.get_rect(center=text_center_pos)
        self.window.blit(surf, rect)






