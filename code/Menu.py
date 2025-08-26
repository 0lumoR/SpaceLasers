import pygame
from pygame import Surface, Rect

from code.Const import WIDTH, WHITE, MENU_OPTION, YELLOW, HEIGHT


class Menu:
    def __init__(self, window):
        self.window = window
        self.bg_img = pygame.image.load("./assets/Background.png").convert_alpha()
        self.bg_y1 = 0
        self.bg_y2 = -HEIGHT
        self.bg_speed = 1  # velocidade do movimento



    def run(self):
        menu_option = 0
        pygame.mixer.music.load('./assets/menuGOsong.mp3')
        pygame.mixer.music.play(-1)


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return "EXIT"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)

                    elif event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)

                    elif event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

            self.bg_y1 += self.bg_speed
            self.bg_y2 += self.bg_speed

            # quando uma imagem sai da tela, volta pro topo
            if self.bg_y1 >= HEIGHT:
                self.bg_y1 = -HEIGHT
            if self.bg_y2 >= HEIGHT:
                self.bg_y2 = -HEIGHT

            # --- desenhar background (duas cópias) ---
            self.window.blit(self.bg_img, (0, self.bg_y1))
            self.window.blit(self.bg_img, (0, self.bg_y2))

            self.menu_text(100, "Space", WHITE, (WIDTH / 2, 100))
            self.menu_text(100, "Lasers", WHITE, (WIDTH / 2, 200))

            for i in range(len(MENU_OPTION)):
                color = YELLOW if i == menu_option else WHITE
                self.menu_text(50, MENU_OPTION[i], color, (WIDTH / 2, 400 + 50 * i))

            pygame.display.flip()



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.Font("./assets/kenvector_future.ttf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


