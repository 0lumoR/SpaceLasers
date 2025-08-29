import pygame
from code.Const import WIDTH, RED, YELLOW, GAME_OVER_OPTIONS, WHITE
from code.EntityFactory import EntityFactory

class GameOver:
    def __init__(self, window, score):
        self.window = window
        self.score = score
        self.player_name = ""  # será digitado pelo jogador
        self.max_chars = 4
        self.bg_layers = EntityFactory.get_backgrounds()
        self.selected = 0
        self.input_mode = True  # True enquanto o jogador digita o nome

    def run(self):
        pygame.mixer.music.load("./assets/menuGOsong.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "EXIT"
                if event.type == pygame.KEYDOWN:
                    if self.input_mode:
                        # Input do nome do jogador
                        if event.key == pygame.K_RETURN and self.player_name:
                            self.input_mode = False  # terminou de digitar
                        elif event.key == pygame.K_BACKSPACE:
                            self.player_name = self.player_name[:-1]
                        elif len(self.player_name) < self.max_chars:
                            if event.unicode.isalnum():  # só letras e números
                                self.player_name += event.unicode.upper()
                    else:
                        # Navegação do menu
                        if event.key == pygame.K_DOWN:
                            self.selected = (self.selected + 1) % len(GAME_OVER_OPTIONS)
                        elif event.key == pygame.K_UP:
                            self.selected = (self.selected - 1) % len(GAME_OVER_OPTIONS)
                        elif event.key == pygame.K_RETURN:
                            return GAME_OVER_OPTIONS[self.selected]

            # Atualizar backgrounds
            for bg in self.bg_layers:
                bg.update()

            # Desenhar backgrounds
            for bg in self.bg_layers:
                self.window.blit(bg.image, bg.rect)

            # Título
            self.menu_text(70, "GAME OVER", RED, (WIDTH // 2, 100), center=True)

            if self.input_mode:
                # Mostrar input de nome
                self.menu_text(40, f"Enter Name: {self.player_name}", YELLOW, (WIDTH // 2, 200), center=True)
            else:
                # Mostrar score e nome do jogador
                self.menu_text(40, f'{self.player_name}: {self.score}', YELLOW, (WIDTH // 2, 200), center=True)
                # Opções do menu
                for i, option in enumerate(GAME_OVER_OPTIONS):
                    color = YELLOW if i == self.selected else WHITE
                    self.menu_text(40, option, color, (WIDTH // 2, 290 + i * 60), center=True)

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, center=False):
        """Desenha texto na tela, similar ao level_text do Level.py"""
        font = pygame.font.Font("./assets/kenvector_future.ttf", text_size)
        surf = font.render(text, True, text_color).convert_alpha()
        rect = surf.get_rect()
        if center:
            rect.center = text_pos
        else:
            rect.topleft = text_pos
        self.window.blit(surf, rect)




