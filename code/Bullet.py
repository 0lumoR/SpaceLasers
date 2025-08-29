from code.Entity import Entity
from code.Const import HEIGHT


class Bullet(Entity):
    def __init__(self, name: str, position: tuple, direction: int, speed: int = 7, dx: int = 0):
        super().__init__(name, position)
        self.speed = speed
        self.direction = direction
        self.dx = dx

    def move(self):
        self.rect.y += self.speed * self.direction
        self.rect.x += self.dx

    def is_off_screen(self):
        return self.rect.bottom < 0 or self.rect.top > HEIGHT

    def update(self):
        self.move()
