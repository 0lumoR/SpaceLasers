import pygame
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, difficulty):
        self.window = window
        self.name = name
        self.bg_layers = EntityFactory.get_backgrounds()
        self.clock = pygame.time.Clock()

    def run(self):

        pygame.mixer.music.load('./assets/levelsong.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()


        while True:
            clock.tick(60)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            for bg in self.bg_layers:
                bg.update()

            # desenhar backgrounds
            for bg in self.bg_layers:
                self.window.blit(bg.image, bg.rect)
            pygame.display.update()




