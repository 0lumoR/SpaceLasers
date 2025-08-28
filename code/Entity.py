import pygame
from abc import ABC

class Entity(ABC, pygame.sprite.Sprite):
    def __init__(self, name: str, position: tuple):
        super().__init__()
        self.name = name
        self.image = pygame.image.load(f"./assets/{name}.png")
        self.rect = self.image.get_rect(topleft=position)
        self.speed = 0

    def move(self):
        pass
