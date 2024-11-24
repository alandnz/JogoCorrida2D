import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Ajusta a imagem para cobrir a tela
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))

    def move(self):
        self.rect.centery += 7  # Velocidade do movimento

        # Reposicionar no topo ao sair da tela
        if self.rect.top >= WIN_HEIGHT:
            self.reset_position()

    def reset_position(self):
        self.rect.bottom = 0
