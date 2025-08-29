import pygame
from code.Const import WIDTH, HEIGHT, WHITE, YELLOW
from code.EntityFactory import EntityFactory


class Score:
    def __init__(self, window, scores=None):
        self.window = window
        self.bg_layers = EntityFactory.get_backgrounds()
        self.scores = scores if scores else []  # lista de placares (date, name, score, time)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return "menu"

            # atualizar backgrounds
            for bg in self.bg_layers:
                bg.update()

            # desenhar backgrounds
            for bg in self.bg_layers:
                self.window.blit(bg.image, bg.rect)

            # título
            self.score_text(50, "SCOREBOARD", YELLOW, (WIDTH // 2, 50))

            # cabeçalho
            self.score_text(25, "DATE", YELLOW, (100, 120))
            self.score_text(25, "NAME", YELLOW, (300, 120))
            self.score_text(25, "SCORE", YELLOW, (500, 120))
            self.score_text(25, "TIME", YELLOW, (700, 120))

            # mostrar scores (apenas top 10)
            for i, entry in enumerate(self.scores[:10]):
                date, name, score, time = entry
                y = 160 + i * 40
                self.score_text(20, str(date), WHITE, (100, y))
                self.score_text(20, str(name), WHITE, (300, y))
                self.score_text(20, str(score), WHITE, (500, y))
                self.score_text(20, str(time), WHITE, (700, y))

            # instrução
            self.score_text(18, "Press ESC to return to menu", WHITE, (WIDTH // 2, HEIGHT - 30))

            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        """Desenha texto na tela, similar ao level_text do Level.py"""
        font = pygame.font.Font("./assets/kenvector_future.ttf", text_size)
        surf = font.render(text, True, text_color).convert_alpha()
        rect = surf.get_rect(center=text_center_pos)
        self.window.blit(surf, rect)
