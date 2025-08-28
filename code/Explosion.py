import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, position, speed=5):
        super().__init__()
        # Carregar imagens da explosão
        self.images = [pygame.image.load(f"./assets/explosion{i}.png").convert_alpha() for i in range(1,3)]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=position)
        self.counter = 0
        self.speed = speed  # controla a rapidez da animação

    def update(self):
        self.counter += 1
        if self.counter % self.speed == 0:
            self.index += 1
            if self.index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.index]
