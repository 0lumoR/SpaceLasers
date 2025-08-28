import pygame
from code.Entity import Entity
from code.Const import ENTITY_SPEED, WIDTH, HEIGHT
import random

class Enemy(Entity):
    def __init__(self, name: str, position):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED.get(name, 2)

    def move(self):
        self.rect.y += self.speed


