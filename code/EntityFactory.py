from random import randint

from code.Background import Background
from code.Const import HEIGHT, WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_backgrounds():
        bgs = []
        for i in range(1, 3):  # LevelBg1 e LevelBg2
            bgs.append(Background(f"LevelBg{i}", (0, 0)))
            bgs.append(Background(f"LevelBg{i}", (0, -HEIGHT)))  # para efeito de scroll contínuo
        return bgs

    @staticmethod
    def get_entity(entity_name: str):
        if entity_name == 'player':
            return [Player('player', (WIDTH // 2, 530))]
        elif entity_name == 'enemy1':
            return [Enemy('enemy1', (randint(40, WIDTH - 100), -100),
                          bullet_type="enemyshot1", bullet_speed=5)]
        elif entity_name == 'enemy2':
            return [Enemy('enemy2', (randint(40, WIDTH - 100), -100),
                          bullet_type="enemyshot2", bullet_speed=7, bullet_dx=-2)]
        elif entity_name == 'enemy3':
            return [Enemy('enemy3', (randint(40, WIDTH - 100), -100),
                          bullet_type="enemyshot3", bullet_speed=8, bullet_dx=2)]
        else:
            return []
