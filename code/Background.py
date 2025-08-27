import pygame
from code.Entity import Entity
from code.Const import ENTITY_SPEED, HEIGHT

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED.get(name, 1)  # pega velocidade da camada

    def move(self):
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT:  # se saiu da tela, volta pra cima
            self.rect.y = -HEIGHT + (self.rect.y - HEIGHT)

