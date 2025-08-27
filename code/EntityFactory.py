from random import randint
from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player
from code.Const import WIDTH, HEIGHT

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'LevelBg':  # vamos usar LevelBg1, 2, 3, 4
                list_bg = []
                for i in range(1, 5):  # LevelBg1 até LevelBg4
                    list_bg.append(Background(f'LevelBg{i}', (0, 0)))
                    list_bg.append(Background(f'LevelBg{i}', (0, HEIGHT)))
                return list_bg

            case 'player':
                return [Player('player', (WIDTH // 2 - 30, HEIGHT - 100))]

            case 'enemy1':
                return [Enemy('enemy1', (randint(40, WIDTH - 40), -50))]

            case 'enemy2':
                return [Enemy('enemy2', (randint(40, WIDTH - 40), -150))]

            case 'enemy3':
                return [Enemy('enemy3', (randint(40, WIDTH - 40), -250))]

            case _:
                return []







