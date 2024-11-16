from code.Entity import Entity


class Obstacle(Entity):
    def __init__(self, image, position: tuple):
        """Inicializa o obstáculo com a imagem fornecida."""
        self.surf = image  # Usa a imagem fornecida
        self.rect = self.surf.get_rect(topleft=position)
        #self.name = "Obstacle"  # Nome genérico para identificação

    def move(self, speed: int):
        """Move o obstáculo para baixo na tela."""
        self.rect.y += speed
