import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.menu_music = './asset/MenuMusic.wav'

    def run(self):
        menu_option = 0
        pygame.mixer_music.load(self.menu_music)
        pygame.mixer_music.set_volume(0.7)  # Reduz o volume da música
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Savanna", C_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Racing", C_ORANGE, ((WIN_WIDTH / 2), 120))
            self.menu_text(20, "Desenvolvido por: Alan Diniz Salazar - RU: 4499264", C_WHITE, ((WIN_WIDTH / 2), 495))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(25, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 230 + 40 * i))
                else:
                    self.menu_text(25, MENU_OPTION[i], C_ORANGE, ((WIN_WIDTH / 2), 230 + 40 * i))
            pygame.display.flip()

            # Checa todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_RETURN:  # Tecla Enter
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Gill Sans", size=text_size, bold=True)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
