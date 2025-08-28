import pygame
from code.Entity import Entity
from code.Const import WIDTH, HEIGHT, ENTITY_SPEED
from code.Bullet import Bullet

class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED[self.name]
        self.rect = self.image.get_rect(center=position)
        self.shoot_cooldown = 500  # tempo mínimo entre tiros (ms)
        self.last_shot = 0

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # manter dentro da tela
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

    def shoot(self, bullets, current_time):
        if current_time - self.last_shot >= self.shoot_cooldown:
            bullet = Bullet("playershot", self.rect.midtop, direction=-1, speed=10)
            bullets.append(bullet)
            self.last_shot = current_time
