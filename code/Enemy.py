from code.Const import ENTITY_SPEED, HEIGHT
from code.Entity import Entity
from random import randint

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def update(self):
        if self.name in ENTITY_SPEED:
            # Move para baixo
            self.rect.y += ENTITY_SPEED[self.name]

            # Se sair da tela, reaparece no topo em posição aleatória horizontal
            if self.rect.top > HEIGHT:
                from code.Const import WIDTH  # importa WIDTH para calcular posição
                self.rect.bottom = 0
                self.rect.x = randint(40, WIDTH - 40)

