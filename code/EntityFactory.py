from code.Background import Background
from code.Const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Road':
                list_bg = []
                # Criar três camadas de fundo, uma centralizada e duas nas laterais
                list_bg.append(Background(f'Road0', (WIN_WIDTH // 2 - 25, 0)))  # Centralizada
                list_bg.append(Background(f'Road1', (0, 0)))  # À esquerda
                list_bg.append(Background(f'Road2', (WIN_WIDTH, 0)))  # À direita
                return list_bg
