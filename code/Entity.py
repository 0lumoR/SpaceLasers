from abc import ABC
import pygame

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load(f'./assets/{name}.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    def update(self):
        """Atualiza a entidade (sobrescrever nas subclasses)"""
        pass

    def draw(self, window):
        """Desenha a entidade na tela"""
        window.blit(self.surf, self.rect)




