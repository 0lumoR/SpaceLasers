from code.Background import Background
from code.Const import WIDTH, HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Background':
                return Background ('Background',WIDTH,HEIGHT)


