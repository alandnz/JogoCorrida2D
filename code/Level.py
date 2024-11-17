import pygame
import random
from code.Const import WIN_WIDTH, WIN_HEIGHT, C_WHITE
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_return):
        self.window = window
        self.name = name
        self.menu_return = menu_return
        self.entity_list = EntityFactory.get_entity('Road')  # Fundo
        self.player = EntityFactory.get_entity('Car', menu_return=menu_return)  # Jogador
        self.obstacles = []  # Lista de obstáculos
        self.obstacle_images = self.load_obstacles()
        self.obstacle_speed = 7
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    @staticmethod
    def load_obstacles():
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
        obstacle_x = random.randint(0, WIN_WIDTH - 50)
        obstacle_y = -100
        image = random.choice(self.obstacle_images)
        obstacle = EntityFactory.get_entity('Obstacle', position=(obstacle_x, obstacle_y), image=image)
        self.obstacles.append(obstacle)

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, C_WHITE)
        self.window.blit(score_text, (10, 10))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def update_obstacles(self):
        for obstacle in self.obstacles[:]:
            obstacle.move(self.obstacle_speed)
            if obstacle.rect.top > WIN_HEIGHT:
                self.obstacles.remove(obstacle)
                self.score += 1

    def detect_collisions(self):
        for obstacle in self.obstacles:
            for obstacle in self.obstacles:
                if self.player.rect.colliderect(obstacle.rect):
                    # Verifica o carro selecionado e carrega a imagem correspondente
                    print(f"menu_return: {self.menu_return}")
                    if self.menu_return == "SINGLE PLAYER - RED":
                        damaged_image = pygame.image.load('./asset/CarRedDam.png').convert_alpha()
                    else:
                        damaged_image = pygame.image.load('./asset/CarYellowDam.png').convert_alpha()

                    # Atualiza a imagem do jogador para a versão danificada
                    self.player.surf = pygame.transform.scale(damaged_image, self.player.surf.get_size())

                    # Redesenha a tela com o carro danificado
                    for ent in self.entity_list:
                        self.window.blit(ent.surf, ent.rect)
                    for obstacle in self.obstacles:
                        self.window.blit(obstacle.surf, obstacle.rect)
                    self.window.blit(self.player.surf, self.player.rect)
                    self.draw_score()

                    # Carrega a imagem "YouLose.png"
                    you_lose_image = pygame.image.load('./asset/YouLose.png').convert_alpha()
                    you_lose_image = pygame.transform.scale(you_lose_image, (WIN_WIDTH / 2, WIN_HEIGHT / 4))

                    # Desenha a imagem "YouLose.png" na tela
                    self.window.blit(you_lose_image, (128, 64))
                    pygame.display.flip()

                    # Aguarda 2 segundos antes de encerrar
                    pygame.time.wait(2000)
                    pygame.quit()
                    exit()

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(45)
            self.handle_events()

            keys = pygame.key.get_pressed()
            self.player.move(keys)

            if random.randint(0, 30) == 0:
                self.generate_obstacle()

            self.update_obstacles()
            self.detect_collisions()

            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()

            for obstacle in self.obstacles:
                self.window.blit(obstacle.surf, obstacle.rect)

            self.window.blit(self.player.surf, self.player.rect)
            self.draw_score()

            pygame.display.flip()
