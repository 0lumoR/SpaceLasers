import pygame
from code.Const import WIDTH, WHITE, YELLOW, MENU_OPTIONS
from code.EntityFactory import EntityFactory


class Menu:
    def __init__(self, window):
        self.window = window
        self.bg_layers = EntityFactory.get_backgrounds()
        self.selected = 0
        self.player_img = pygame.image.load("./assets/player.png")
        self.player_rect = self.player_img.get_rect(center=(WIDTH // 2, 550))

    def run(self):
        pygame.mixer.music.load("./assets/menuGOsong.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(MENU_OPTIONS)
                    elif event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(MENU_OPTIONS)
                    elif event.key == pygame.K_RETURN:
                        return MENU_OPTIONS[self.selected]

            # atualizar backgrounds
            for bg in self.bg_layers:
                bg.update()

            # desenhar backgrounds
            for bg in self.bg_layers:
                self.window.blit(bg.image, bg.rect)

            # nave decorativa
            self.window.blit(self.player_img, self.player_rect)

            # título
            self.menu_text(70, "SPACE LASERS", WHITE, (WIDTH // 2, 100), center=True)

            # opções do menu
            for i, option in enumerate(MENU_OPTIONS):
                color = YELLOW if i == self.selected else WHITE
                self.menu_text(40, option, color, (WIDTH // 2, 290 + i * 60), center=True)

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, center=False):
        """Desenha texto na tela, similar ao level_text do Level.py"""
        font = pygame.font.Font("./assets/kenvector_future.ttf", text_size)
        surf = font.render(text, True, text_color).convert_alpha()
        rect = surf.get_rect()
        if center:
            rect.center = text_pos
        else:
            rect.topleft = text_pos
        self.window.blit(surf, rect)


