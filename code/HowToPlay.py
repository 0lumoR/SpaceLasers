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
        self.spacebar_rect = self.spacebar_img.get_rect(center=(WIDTH // 2 + 100, HEIGHT // 2 + 100))

        self.ctrl_img = pygame.image.load("./assets/ctrl.png")
        self.ctrl_img = pygame.transform.scale(self.ctrl_img, (150, 100))
        self.ctrl_rect = self.ctrl_img.get_rect(center=(WIDTH // 2 - 100, HEIGHT // 2 + 100))

        # imagem do WASD
        self.wasd_img = pygame.image.load("./assets/wasd.png")
        self.wasd_img = pygame.transform.scale(self.wasd_img, (150, 100))
        self.wasd_rect = self.wasd_img.get_rect(center=(WIDTH // 2 - 100, HEIGHT // 2 - 50))

        # imagem das setas
        self.arrowkeys_img = pygame.image.load("./assets/arrowkeys.png")
        self.arrowkeys_img = pygame.transform.scale(self.arrowkeys_img, (150, 100))
        self.arrowkeys_rect = self.arrowkeys_img.get_rect(center=(WIDTH // 2 + 100, HEIGHT // 2 - 50))

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

            # textos explicativos
            self.game_over_text(50, "HOW TO PLAY", WHITE, (WIDTH // 2, 50))
            self.game_over_text(30, "Move with WASD or arrow keys", WHITE, (WIDTH // 2, HEIGHT // 2 - 120))
            self.game_over_text(30, "Shoot with RCTRL or SPACEBAR", WHITE, (WIDTH // 2, HEIGHT // 2 + 30))
            self.game_over_text(15, "Press Esc to go back to menu", WHITE, (WIDTH // 2, HEIGHT - 20))

            # desenhar imagens redimensionadas
            self.window.blit(self.wasd_img, self.wasd_rect)
            self.window.blit(self.arrowkeys_img, self.arrowkeys_rect)
            self.window.blit(self.spacebar_img, self.spacebar_rect)
            self.window.blit(self.ctrl_img, self.ctrl_rect)

            pygame.display.flip()

    def game_over_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        font = pygame.font.Font("./assets/kenvector_future.ttf", text_size)
        surf = font.render(text, True, text_color).convert_alpha()
        rect = surf.get_rect(center=text_center_pos)
        self.window.blit(surf, rect)
