from code.Background import Background
from code.Car import Car
from code.Obstacle import Obstacle
from code.Const import WIN_HEIGHT


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0), **kwargs):
        match entity_name:
            case 'Road':
                return [
                    Background('Road', (0, 0)),
                    Background('Road', (0, -WIN_HEIGHT)),
                ]
            case 'Car':
                return Car(kwargs['menu_return'], position)
            case 'Obstacle':
                return Obstacle(kwargs['image'], position)

