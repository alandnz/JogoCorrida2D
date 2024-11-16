import pygame
import random

from code.Const import WIN_WIDTH, WIN_HEIGHT, C_WHITE, MENU_OPTION
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_return):
        self.window = window
        self.name = name
        self.menu_return = menu_return
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Road'))

        # Inicializações
        self.car_image, self.player_speed = self.load_player_car()
        self.car_rect = self.car_image.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT - 75))
        self.obstacles = []
        self.obstacle_images = self.load_obstacles()
        self.obstacle_speed = 7
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def load_player_car(self):
        """Carrega a imagem e configura a velocidade do carro do jogador."""
        if self.menu_return == MENU_OPTION[0]:  # Red car
            car_image = pygame.image.load('./asset/CarRed.png').convert_alpha()
            player_speed = 10
            pygame.mixer_music.load('./asset/Level1.wav')
            pygame.mixer_music.play(-1)
        elif self.menu_return == MENU_OPTION[1]:  # Yellow car
            car_image = pygame.image.load('./asset/CarYellow.png').convert_alpha()
            player_speed = 15
            pygame.mixer_music.load('./asset/Level2.wav')
            pygame.mixer_music.play(-1)
        car_image = pygame.transform.scale(car_image, (50, 100))
        return car_image, player_speed

    @staticmethod
    def load_obstacles():
        """Carrega e redimensiona as imagens dos obstáculos."""
        obstacle_paths = [
            ('./asset/Tree01.png', (100, 125)),
            ('./asset/Tree02.png', (75, 100)),
            ('./asset/Tree03.png', (50, 75)),
            ('./asset/Tree04.png', (50, 125)),
        ]
        return [
            pygame.transform.scale(pygame.image.load(path).convert_alpha(), size)
            for path, size in obstacle_paths
        ]

    def generate_obstacle(self):
        """Gera um obstáculo em posição aleatória."""
        obstacle_x = random.randint(0, WIN_WIDTH - 50)
        obstacle_y = -100
        obstacle_type = random.choice(self.obstacle_images)
        self.obstacles.append([obstacle_x, obstacle_y, obstacle_type])

    def draw_score(self):
        """Desenha a pontuação na tela."""
        score_text = self.font.render(f"Score: {self.score}", True, C_WHITE)
        self.window.blit(score_text, (10, 10))

    def handle_events(self):
        """Processa os eventos do Pygame."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def move_player(self, keys):
        """Move o carro do jogador com base nas teclas pressionadas."""
        if keys[pygame.K_LEFT] and self.car_rect.left > 0:
            self.car_rect.x -= self.player_speed
        if keys[pygame.K_RIGHT] and self.car_rect.right < WIN_WIDTH:
            self.car_rect.x += self.player_speed

    def update_obstacles(self):
        """Atualiza a posição dos obstáculos e verifica colisões."""
        for obstacle in self.obstacles[:]:
            obstacle[1] += self.obstacle_speed
            if obstacle[1] > WIN_HEIGHT:
                self.obstacles.remove(obstacle)
                self.score += 1

    def detect_collisions(self):
        """Detecta colisões entre o jogador e os obstáculos."""
        for obstacle in self.obstacles:
            obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], *obstacle[2].get_size())
            if self.car_rect.colliderect(obstacle_rect):
                # Jogar som de colisão e encerrar o jogo (som desativado por enquanto)
                pygame.time.wait(1000)
                pygame.quit()
                exit()

    def run(self):
        """Executa o loop principal do nível."""
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(45)
            self.handle_events()

            keys = pygame.key.get_pressed()
            self.move_player(keys)

            if random.randint(0, 30) == 0:
                self.generate_obstacle()

            self.update_obstacles()
            self.detect_collisions()

            # Renderização
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()

            for obstacle in self.obstacles:
                self.window.blit(obstacle[2], (obstacle[0], obstacle[1]))

            self.window.blit(self.car_image, self.car_rect)
            self.draw_score()

            pygame.display.flip()