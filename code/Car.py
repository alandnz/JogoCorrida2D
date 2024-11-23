import pygame
from code.Entity import Entity
from code.Const import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT


class Car(Entity):
    def __init__(self, menu_return: str, position: tuple):
        super().__init__('CarRed' if menu_return == MENU_OPTION[0] else 'CarYellow', position)
        self.speed = 10 if menu_return == MENU_OPTION[0] else 15
        self.surf = pygame.transform.scale(self.surf, (50, 100))  # Tamanho do carro
        self.rect = self.surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT - 75))  # Posição do carro
        self.load_music(menu_return)

    def load_music(self, menu_return: str):
        if menu_return == MENU_OPTION[0]:
            pygame.mixer_music.load('./asset/Level1.wav')
        elif menu_return == MENU_OPTION[1]:
            pygame.mixer_music.load('./asset/Level2.wav')
        pygame.mixer_music.play(-1)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 75:  # Controle das bordas laterais
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH - 75:
            self.rect.x += self.speed
