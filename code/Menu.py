import pygame
from code.Const import WIDTH, WHITE, YELLOW, MENU_OPTIONS, HEIGHT, PLAYER_KEY_UP, PLAYER_KEY_DOWN, MENU_KEY_SELECT
from code.EntityFactory import EntityFactory


class Menu:
    def __init__(self, window):
        self.window = window
        self.bg_layers = EntityFactory.get_backgrounds()
        self.selected = 0
        self.player_img = pygame.image.load("./assets/player.png")
        self.player_rect = self.player_img.get_rect(center=(WIDTH // 2, 530))

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return quit()
                if event.type == pygame.KEYDOWN:
                    if event.key in PLAYER_KEY_DOWN:
                        self.selected = (self.selected + 1) % len(MENU_OPTIONS)
                    elif event.key in PLAYER_KEY_UP:
                        self.selected = (self.selected - 1) % len(MENU_OPTIONS)
                    elif event.key in MENU_KEY_SELECT:
                        return MENU_OPTIONS[self.selected]

            # atualizar backgrounds
            for bg in self.bg_layers:
                bg.update()

            for bg in self.bg_layers:
                self.window.blit(bg.image, bg.rect)

            self.window.blit(self.player_img, self.player_rect)

            # título
            self.menu_text(70, "SPACE LASERS", WHITE, (WIDTH // 2, 100))
            self.menu_text(15, "Press Enter or Space to select options", WHITE, (WIDTH // 2, HEIGHT - 20))

            # opções
            for i, option in enumerate(MENU_OPTIONS):
                color = YELLOW if i == self.selected else WHITE
                self.menu_text(40, option, color, (WIDTH // 2, 290 + i * 60))

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        font = pygame.font.Font("./assets/kenvector_future.ttf", text_size)
        surf = font.render(text, True, text_color).convert_alpha()
        rect = surf.get_rect(center=text_center_pos)
        self.window.blit(surf, rect)

