import pygame
import random
import time

from code.Const import WIN_WIDTH, WIN_HEIGHT, C_YELLOW, C_ROAD_COLOR, C_WHITE, MENU_OPTION


class Level:
    def __init__(self, window, name, menu_return):
        self.window = window
        self.name = name
        self.menu_return = menu_return  # Escolha do menu

    def run(self):
        # Sons
        # collision_sound = pygame.mixer.Sound("collision.wav")
        # engine_sound = pygame.mixer.Sound("engine.wav")
        # engine_sound.set_volume(0.5)
        # engine_sound.play(-1)  # Reproduzir o som do motor em loop

        # Configurações do carro do jogador
        if self.menu_return == MENU_OPTION[0]:  # Red car
            car_image = pygame.image.load('./asset/CarRed.png')
            player_speed = 10
        elif self.menu_return == MENU_OPTION[1]:  # Yellow car
            car_image = pygame.image.load('./asset/CarYellow.png')
            player_speed = 15  # Velocidade superior ao carro Red

        # Escala e posição do carro
        car_image = pygame.transform.scale(car_image, (50, 100))
        player_x = WIN_WIDTH // 2 - 25
        player_y = WIN_HEIGHT - 150

        # Configurações dos obstáculos
        obstacle01 = pygame.image.load('./asset/Tree01.png')
        obstacle01 = pygame.transform.scale(obstacle01, (100, 125))
        obstacle02 = pygame.image.load('./asset/Tree02.png')
        obstacle02 = pygame.transform.scale(obstacle02, (75, 100))
        obstacle03 = pygame.image.load('./asset/Tree03.png')
        obstacle03 = pygame.transform.scale(obstacle03, (50, 75))
        obstacle04 = pygame.image.load('./asset/Tree04.png')
        obstacle04 = pygame.transform.scale(obstacle04, (50, 125))
        obstacle_speed = 7
        obstacles = []

        # Fonte para pontuação
        font = pygame.font.Font(None, 36)

        # Função para desenhar a estrada
        def draw_road():
            self.window.fill(C_ROAD_COLOR)
            pygame.draw.rect(self.window, C_YELLOW, (WIN_WIDTH // 2 - 5, 0, 10, WIN_HEIGHT))

        # Função para gerar obstáculos
        def generate_obstacle():
            obstacle_x = random.randint(0, WIN_WIDTH - 50)
            obstacle_y = -100
            # Escolher aleatoriamente entre as duas imagens
            obstacle_type = random.choice([obstacle01, obstacle02, obstacle03, obstacle04])
            obstacles.append([obstacle_x, obstacle_y, obstacle_type])

        # Função para desenhar a pontuação
        def draw_score(score):
            score_text = font.render(f"Score: {score}", True, C_WHITE)
            self.window.blit(score_text, (10, 10))

        # Variáveis do jogo
        clock = pygame.time.Clock()
        score = 0
        running = True

        # Loop principal do jogo
        while running:
            clock.tick(30)  # Controla a taxa de quadros
            draw_road()

            # Eventos do Pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Movimentação do carro do jogador
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_x > 0:
                player_x -= player_speed
            if keys[pygame.K_RIGHT] and player_x < WIN_WIDTH - 50:
                player_x += player_speed

            # Gerar novos obstáculos e atualizar posição
            if random.randint(0, 30) == 0:  # 1/30 de chance de gerar obstáculo a cada frame
                generate_obstacle()
            for obstacle in obstacles:
                obstacle[1] += obstacle_speed  # Movimenta o obstáculo para baixo
                if obstacle[1] > WIN_HEIGHT:
                    obstacles.remove(obstacle)
                    score += 1  # Aumenta pontuação ao evitar um obstáculo

            # Desenhar obstáculos e detectar colisão
            for obstacle in obstacles:
                # Desenha o obstáculo baseado no tipo
                self.window.blit(obstacle[2], (obstacle[0], obstacle[1]))
                # Detecta colisão entre o carro do jogador e o obstáculo
                if (player_x < obstacle[0] + 50 and
                        player_x + 50 > obstacle[0] and
                        player_y < obstacle[1] + 100 and
                        player_y + 100 > obstacle[1]):
                    collision_sound.play()
                    time.sleep(1)  # Pausa para o som de colisão
                    running = False

            # Desenhar o carro do jogador e a pontuação
            self.window.blit(car_image, (player_x, player_y))
            draw_score(score)

            pygame.display.flip()

        # Encerrar o jogo e Pygame
        engine_sound.stop()
        pygame.quit()
