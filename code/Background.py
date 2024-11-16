from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.offset = position[0]  # Definir o deslocamento inicial horizontal

    def move(self):
        self.rect.centery += 5  # Move a imagem para baixo

        # Quando a imagem ultrapassar o fundo (passar para baixo da tela), reposiciona no topo
        if self.rect.top >= WIN_HEIGHT:
            self.rect.bottom = 0  # Move para o topo
            self.rect.centerx = self.offset  # Mantém a posição horizontal do "parallax"
