import pygame

# Tamanho da tela
WIDTH, HEIGHT = 900, 600

# Menu opções
MENU_OPTIONS = ("START GAME", "HOW TO PLAY", "SCORE", "EXIT")
GAME_OVER_OPTIONS = ("TRY AGAIN", "BACK TO MENU", "EXIT")

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 220, 90)

# Velocidades
ENTITY_SPEED = {
    'player': 5,
    'enemy1': 2,
    'enemy2': 2,
    'enemy3': 2,
    'LevelBg1': 1,
    'LevelBg2': 2,
}


# Movimento
PLAYER_KEY_UP = [pygame.K_UP, pygame.K_w]
PLAYER_KEY_DOWN = [pygame.K_DOWN, pygame.K_s]
PLAYER_KEY_LEFT = [pygame.K_LEFT, pygame.K_a]
PLAYER_KEY_RIGHT = [pygame.K_RIGHT, pygame.K_d]

# Ações
PLAYER_KEY_SHOOT = [pygame.K_SPACE,pygame.K_RCTRL]
MENU_KEY_SELECT = [pygame.K_RETURN, pygame.K_SPACE]
MENU_KEY_BACK = [pygame.K_ESCAPE]
