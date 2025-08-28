import pygame
import random
from pygame.font import Font
from pygame import Surface, Rect

from code.Const import WHITE, HEIGHT, WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, difficulty):
        self.window = window
        self.name = name
        self.bg_layers = EntityFactory.get_backgrounds()
        self.clock = pygame.time.Clock()

        # entidades
        self.entity_list: list[Entity] = []
        self.player = EntityFactory.get_entity('player')
        self.entity_list.append(self.player)

        # lista só para inimigos
        self.enemies: list[Entity] = []
        self.spawn_timer = 0  # contador para spawn gradual

    def run(self):
        pygame.mixer.music.load('./assets/levelsong.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        running = True
        while running:
            dt = self.clock.tick(60)  # delta time em ms

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # atualizar backgrounds
            for bg in self.bg_layers:
                bg.update()

            # movimentar entidades
            self.player.move()
            for enemy in self.enemies:
                enemy.move()

            # remover inimigos que saíram da tela
            self.enemies = [enemy for enemy in self.enemies if enemy.rect.top <= HEIGHT]

            # controlar spawn (a cada ~2 segundos nasce um inimigo)
            self.spawn_timer += dt
            if self.spawn_timer > 2000:  # 2000 ms = 2 segundos
                enemy_type = f'enemy{random.randint(1,3)}'
                new_enemy = EntityFactory.get_entity(enemy_type, (random.randint(0, WIDTH-50), -50))
                self.enemies.append(new_enemy)
                self.spawn_timer = 0

            # # --- DESENHO ---
            # self.window.fill((0, 0, 0))

            # desenhar backgrounds
            for bg in self.bg_layers:
                self.window.blit(bg.image, bg.rect)

            # desenhar player
            self.window.blit(self.player.image, self.player.rect)

            # desenhar inimigos
            for enemy in self.enemies:
                self.window.blit(enemy.image, enemy.rect)

            # HUD
            self.level_text(20, f'fps: {self.clock.get_fps():.0f}', WHITE, (10, HEIGHT - 35))
            self.level_text(20, f'inimigos ativos: {len(self.enemies)}', WHITE, (10, HEIGHT - 20))

            pygame.display.flip()

        pygame.quit()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Arial", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

