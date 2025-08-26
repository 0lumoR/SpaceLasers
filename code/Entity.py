from abc import ABC

import pygame


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.Bg').convert_alpha()
        self.speed = 0