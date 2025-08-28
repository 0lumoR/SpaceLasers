from random import randint

from code.Background import Background
from code.Const import HEIGHT, WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_backgrounds():
        bgs = []
        for i in range(1, 3):  # LevelBg1 até LevelBg4
            bgs.append(Background(f"LevelBg{i}", (0, 0)))
            bgs.append(Background(f"LevelBg{i}", (0, -HEIGHT)))
        return bgs

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'player':
                return Player('player', (WIDTH // 2 , 550))
            case 'enemy1':
                return Enemy('enemy1', (randint(0, WIDTH - 100), randint(-300, -50)))
            case 'enemy2':
                return Enemy('enemy2', (randint(0, WIDTH - 100), randint(-300, -50)))
            case 'enemy3':
                return Enemy('enemy3', (randint(0, WIDTH - 100), randint(-300, -50)))
            case _:
                return None
