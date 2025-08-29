import pygame
from code.Const import WIDTH, WHITE, HEIGHT
from code.EntityFactory import EntityFactory


class HowToPlay:
    def __init__(self, window):
        self.window = window
        self.bg_layers = EntityFactory.get_backgrounds()
        self.selected = 0

        # carregar e redimensionar imagens
        self.spacebar_img = pygame.image.load("./assets/spacebar.png")
        self.spacebar_img = pygame.transform.scale(self.spacebar_img, (200, 80))  # largura x altura
        self.spacebar_rect = self.spacebar_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

        self.arrowkeys_img = pygame.image.load("./assets/arrowkeys.png")
        self.arrowkeys_img = pygame.transform.scale(self.arrowkeys_img, (150, 100))
        self.arrowkeys_rect = self.arrowkeys_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

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
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return "menu"

            # atualizar backgrounds
            for bg in self.bg_layers:
                bg.update()

            # desenhar backgrounds
            for bg in self.bg_layers:
                self.window.blit(bg.image, bg.rect)

            # textos explicativos
            self.menu_text(50, "HOW TO PLAY", WHITE, (WIDTH // 2, 50), center=True)
            self.menu_text(30, "Move with arrow keys", WHITE, (WIDTH // 2, HEIGHT // 2 - 120), center=True)
            self.menu_text(30, "Shoot with SPACEBAR", WHITE, (WIDTH // 2, HEIGHT // 2 + 30), center=True)
            self.menu_text(15, "Press Esc to go back to menu", WHITE, (WIDTH // 2, HEIGHT - 20), center=True)

            # desenhar imagens redimensionadas
            self.window.blit(self.arrowkeys_img, self.arrowkeys_rect)
            self.window.blit(self.spacebar_img, self.spacebar_rect)

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
