import pygame
from pygame import Surface, Rect
from code.Const import WIDTH, WHITE, MENU_OPTION, YELLOW
from code.EntityFactory import EntityFactory


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/Background.png').convert_alpha()
        self.rect = self.surf.get_rect(topleft=(0, 0))


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


            self.window.blit(self.surf, self.rect)
            self.menu_text(100, "Space", WHITE, (WIDTH / 2, 100))
            self.menu_text(100, "Lasers", WHITE, (WIDTH / 2, 200))

            for i in range(len(MENU_OPTION)):
                color = YELLOW if i == menu_option else WHITE
                self.menu_text(50, MENU_OPTION[i], color, (WIDTH / 2, 400 + 50 * i))

            pygame.display.flip()

    def create_entities(scene_type):
        entities = pygame.sprite.Group()

        # background sempre presente
        background = EntityFactory.create("background")
        entities.add(background)

        # estrelas para menu ou level
        for _ in range(20):
            star = EntityFactory.create("star")
            entities.add(star)

        # meteoros só no level
        if scene_type == "level":
            for _ in range(5):
                meteor = EntityFactory.create("meteor")
                entities.add(meteor)

        return entities

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.Font("./assets/kenvector_future.ttf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


