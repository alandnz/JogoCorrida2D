import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                level = Level(self.window, 'Level', menu_return)
                level_return = level.run()

                # Se retornar 'MENU' após a colisão, recarrega o Menu
                if level_return == 'MENU':
                    continue

            elif menu_return == MENU_OPTION[3]:
                pygame.quit()
                quit()
            else:
                pass