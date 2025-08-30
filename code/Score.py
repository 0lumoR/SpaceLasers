import pygame
from code.Const import WIDTH, HEIGHT, WHITE, YELLOW
from code.EntityFactory import EntityFactory
from code.DBProxy import DBProxy

class Score:
    def __init__(self, window):
        self.window = window
        self.bg_layers = EntityFactory.get_backgrounds()
        self.db = DBProxy("scores.db")
        self.scores = self.db.get_top_scores(10)  # busca top 10 do banco

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False  # volta para o menu

            # --- fundo animado ---
            for bg in self.bg_layers:
                bg.update()
                self.window.blit(bg.image, bg.rect)

            # --- título ---
            self.score_text(50, "SCOREBOARD", YELLOW, (WIDTH // 2, 50))

            # --- cabeçalho ---
            self.score_text(25, "DATE", YELLOW, (150, 120))
            self.score_text(25, "NAME", YELLOW, (350, 120))
            self.score_text(25, "SCORE", YELLOW, (550, 120))
            self.score_text(25, "TIME", YELLOW, (750, 120))

            # --- lista de scores ---
            for i, entry in enumerate(self.scores):
                name, score, elapsed_time, date = entry  # ordem correta
                y = 160 + i * 40

                # converter segundos → MM:SS
                minutes = elapsed_time // 60
                seconds = elapsed_time % 60
                time_str = f"{minutes:02}:{seconds:02}"

                self.score_text(20, str(date), WHITE, (150, y))
                self.score_text(20, str(name), WHITE, (350, y))
                self.score_text(20, str(score), WHITE, (550, y))
                self.score_text(20, time_str, WHITE, (750, y))

            # --- instrução ---
            self.score_text(20, "PRESS ESC TO RETURN TO MENU", WHITE, (WIDTH // 2, HEIGHT - 30))

            pygame.display.flip()

    def score_text(self, size, text, color, pos):
        font = pygame.font.Font("./assets/kenvector_future.ttf", size)
        surf = font.render(text, True, color).convert_alpha()
        rect = surf.get_rect(center=pos)
        self.window.blit(surf, rect)


