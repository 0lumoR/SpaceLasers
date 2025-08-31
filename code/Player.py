import pygame
from code.Const import WIDTH, HEIGHT, ENTITY_SPEED, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, \
    PLAYER_KEY_SHOOT
from code.Entity import Entity
from code.Bullet import Bullet

class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED[self.name]
        self.rect = self.image.get_rect(center=position)

        self.shoot_cooldown = 300
        self.last_shot = 0
        self.bullets = pygame.sprite.Group()
        self.health = 3

        self.shoot_sound = pygame.mixer.Sound("./assets/lasersfx.ogg")
        self.shoot_sound.set_volume(0.3)

    def move(self, keys):
        dx, dy = 0, 0
        keys = pygame.key.get_pressed()

        if any(keys[key] for key in PLAYER_KEY_LEFT) and self.rect.left > 0:
            self.rect.x -= self.speed
        if any(keys[key] for key in PLAYER_KEY_RIGHT) and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if any(keys[key] for key in PLAYER_KEY_UP) and self.rect.top > 0:
            self.rect.y -= self.speed
        if any(keys[key] for key in PLAYER_KEY_DOWN) and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

        self.rect.x += dx
        self.rect.y += dy

    def shoot(self, keys):
        if any(keys[key] for key in PLAYER_KEY_SHOOT):
            now = pygame.time.get_ticks()
            if now - self.last_shot >= self.shoot_cooldown:
                self.last_shot = now
                bullet = Bullet("playershot", self.rect.center, -1)
                self.bullets.add(bullet)
                self.shoot_sound.play()

    def update(self, keys):
        self.move(keys)
        self.shoot(keys)
