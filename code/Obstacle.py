from code.Entity import Entity


class Obstacle(Entity):
    def __init__(self, image, position: tuple):
        # Inicializa o obstáculo com a imagem recebida
        self.surf = image
        self.rect = self.surf.get_rect(topleft=position)

    def move(self, speed: int):
        self.rect.y += speed
