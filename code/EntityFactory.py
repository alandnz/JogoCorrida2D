from code.Background import Background
from code.Const import WIN_HEIGHT

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Road':
                list_bg = [
                    Background('Road', (0, 0)),  # Primeira imagem
                    Background('Road', (0, -WIN_HEIGHT))  # Segunda imagem posicionada acima
                ]
                return list_bg
