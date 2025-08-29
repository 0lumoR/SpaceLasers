# Background.py
import pygame
from code.Entity import Entity
from code.Const import HEIGHT, ENTITY_SPEED


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED.get(name, 1)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT:
            self.rect.y = -HEIGHT + (self.rect.y - HEIGHT)
