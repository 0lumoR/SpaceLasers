import pygame
from code.Const import WIDTH, WHITE, YELLOW, MENU_OPTIONS
from code.EntityFactory import EntityFactory


class Menu:
    def __init__(self, window):
        self.window = window
        self.bg_layers = EntityFactory.get_backgrounds()
        self.font = pygame.font.Font("./assets/kenvector_future.ttf", 40)
        self.title_font = pygame.font.Font("./assets/kenvector_future.ttf", 70)
        self.selected = 0
        self.player_img = pygame.image.load("./assets/player.png").convert_alpha()
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
            title = self.title_font.render("SPACE LASERS", True, WHITE)
            self.window.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

            # opções
            for i, option in enumerate(MENU_OPTIONS):
                color = YELLOW if i == self.selected else WHITE
                surf = self.font.render(option, True, color)
                self.window.blit(surf, (WIDTH // 2 - surf.get_width() // 2, 290 + i * 60))

            pygame.display.flip()
