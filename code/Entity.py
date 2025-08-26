from abc import ABC

import pygame

class Entity():
    class Entity(ABC):
        def __init__(self, name: str, position: tuple):
            self.name = name
            self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
            self.rect = self.surf.get_rect(lefttop=position)
            self.speed = 0



