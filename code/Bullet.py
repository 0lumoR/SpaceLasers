import pygame
from code.Entity import Entity
from code.Const import HEIGHT

class Bullet(Entity):
    def __init__(self, name: str, position: tuple, direction: int, speed: int = 7, dx: int = 0):
        """
        :param name: nome da imagem (ex: 'bullet_player', 'bullet_enemy1', 'bullet_enemy2')
        :param position: posição inicial
        :param direction: -1 = pra cima, +1 = pra baixo
        :param speed: velocidade vertical
        :param dx: deslocamento horizontal (padrões diferentes de tiro)
        """
        super().__init__(name, position)
        self.speed = speed
        self.direction = direction
        self.dx = dx  # velocidade lateral

    def move(self):
        self.rect.y += self.speed * self.direction
        self.rect.x += self.dx  # pode andar na horizontal também

    def is_off_screen(self):
        return self.rect.bottom < 0 or self.rect.top > HEIGHT
