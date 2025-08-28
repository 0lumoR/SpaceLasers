import random
import pygame
from code.Entity import Entity
from code.Bullet import Bullet

class Enemy(Entity):
    def __init__(self, name: str, position, bullet_type="bullet_enemy", shoot_chance=0.01,
                 bullet_speed=6, bullet_dx=0, shoot_cooldown=1000):
        super().__init__(name, position)
        self.speed = 2
        self.bullet_type = bullet_type
        self.shoot_chance = shoot_chance
        self.bullet_speed = bullet_speed
        self.bullet_dx = bullet_dx

        # cooldown de tiro
        self.last_shot_time = 0
        self.shoot_cooldown = shoot_cooldown  # em ms

    def move(self):
        self.rect.y += self.speed

    def try_shoot(self, bullets):
        current_time = pygame.time.get_ticks()
        if random.random() < self.shoot_chance and current_time - self.last_shot_time > self.shoot_cooldown:
            bullet = Bullet(
                name=self.bullet_type,
                position=self.rect.midbottom,
                direction=1,
                speed=self.bullet_speed,
                dx=self.bullet_dx
            )
            bullets.append(bullet)
            self.last_shot_time = current_time

