import pygame
from code.Const import HEIGHT

class Life(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("./assets/life.png").convert_alpha()  # sua imagem de coração
        self.image = pygame.transform.scale(self.image, (40, 40))  # tamanho opcional
        self.rect = self.image.get_rect(center=pos)
        self.speed = 3  # velocidade de queda

    def update(self):
        self.rect.y += self.speed
        # remover se sair da tela
        if self.rect.top > HEIGHT:
            self.kill()
