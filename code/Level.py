import pygame
from pygame import Surface
from code.EntityFactory import EntityFactory
from code.Entity import Entity
from code.Const import HEIGHT, WIDTH

class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, bg_speed: int = 1):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.bg_speed = bg_speed

        # Background
        self.bg_img = pygame.image.load("./assets/Background.png").convert_alpha()
        self.bg_y1 = 0
        self.bg_y2 = -HEIGHT

        # Lista de entidades
        self.entity_list: list[Entity] = []

        # Adiciona player
        self.entity_list.extend(EntityFactory.get_entity('player'))

        # Adiciona inimigos
        self.entity_list.extend(EntityFactory.get_entity('enemy1'))
        self.entity_list.extend(EntityFactory.get_entity('enemy2'))
        self.entity_list.extend(EntityFactory.get_entity('enemy3'))

    def run(self):
        # Música de fundo
        pygame.mixer.music.load('./assets/levelsong.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(60)

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Movimento do background
            self.bg_y1 += self.bg_speed
            self.bg_y2 += self.bg_speed

            if self.bg_y1 >= HEIGHT:
                self.bg_y1 = -HEIGHT
            if self.bg_y2 >= HEIGHT:
                self.bg_y2 = -HEIGHT

            # Desenhar background
            self.window.blit(self.bg_img, (0, self.bg_y1))
            self.window.blit(self.bg_img, (0, self.bg_y2))

            # Atualizar e desenhar todas as entidades
            for entity in self.entity_list:
                entity.update()
                entity.draw(self.window)

            pygame.display.update()

        # Retorna ao Game sem fechar o Pygam