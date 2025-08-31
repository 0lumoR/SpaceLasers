import pygame
from code.Const import WIDTH, HEIGHT, WHITE, YELLOW, MENU_KEY_SELECT, MENU_KEY_BACK, PLAYER_KEY_UP, PLAYER_KEY_DOWN
from code.EntityFactory import EntityFactory


class GameOver:
    def __init__(self, window, score):
        self.window = window
        self.score = score
        self.bg_layers = EntityFactory.get_backgrounds()
        self.selected = 0
        self.options = ["Retry", "Menu", "Quit"]

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key in PLAYER_KEY_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)
                    elif event.key in PLAYER_KEY_UP:
                        self.selected = (self.selected - 1) % len(self.options)
                    elif event.key in MENU_KEY_SELECT:
                        return self.options[self.selected]
                    elif event.key in MENU_KEY_BACK:
                        return "menu"

            for bg in self.bg_layers:
                bg.update()
                self.window.blit(bg.image, bg.rect)

            # textos
            self.draw_text(70, "GAME OVER", WHITE, (WIDTH // 2, 100))
            self.draw_text(30, f"Score: {self.score}", WHITE, (WIDTH // 2, 180))

            for i, option in enumerate(self.options):
                color = YELLOW if i == self.selected else WHITE
                self.draw_text(40, option, color, (WIDTH // 2, 300 + i * 60))

            pygame.display.flip()

    def draw_text(self, size, text, color, pos):
        font = pygame.font.Font("./assets/kenvector_future.ttf", size)
        surf = font.render(text, True, color).convert_alpha()
        rect = surf.get_rect(center=pos)
        self.window.blit(surf, rect)








