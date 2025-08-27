from code.Background import Background
from code.Const import HEIGHT

class EntityFactory:
    @staticmethod
    def get_backgrounds():
        bgs = []
        for i in range(1, 5):  # LevelBg1 até LevelBg4
            bgs.append(Background(f"LevelBg{i}", (0, 0)))
            bgs.append(Background(f"LevelBg{i}", (0, -HEIGHT)))
        return bgs








